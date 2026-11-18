#!/usr/bin/env python3
"""Compile the reviewed Markdown questions into Moodle XML, Forms import PDFs, and the self-check page."""
import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.dom.minidom import Document

from pypdf import PdfReader

import self_check
from formatting import ascii_text, inline, to_html
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Preformatted, Spacer, PageBreak, KeepTogether,
                                HRFlowable)

ROOT = Path(__file__).resolve().parents[1]
TITLES = {1: 'Infrastructure as Code concepts', 2: 'Images and machine initialization',
          3: 'Server state and configuration organization',
          4: 'Resilience and verifying configuration code',
          5: 'Declarative cloud provisioning and state',
          6: 'Choosing cloud deployment options',
          7: 'Modules, testing, and automated quality checks',
          8: 'Module versioning and interface design',
          9: 'GitOps, pipelines, and team workflows'}

# eXtreme Automation (XA) design tokens used by the human-facing outputs.
XA = {'rose': '#d27079', 'navy': '#3d496e', 'slate': '#535c73', 'muted': '#8991a8', 'ink': '#212121',
      'line': '#e9e9ef', 'rose_soft': '#f7e6e8'}
FONTS = {'PTSans': 'ptsans/PT_Sans-Web-Regular.ttf', 'PTSans-Bold': 'ptsans/PT_Sans-Web-Bold.ttf',
         'JetBrainsMono': 'jetbrainsmono/JetBrainsMono[wght].ttf'}
# Each lecture PDF starts a new page before these questions, giving four pages per lecture.
PAGE_BREAKS = (5, 7, 9)
SELF_CHECK = ROOT/'self-check/index.html'


def register_fonts():
    for name, path in FONTS.items():
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, str(ROOT/'assets/fonts'/path)))
    pdfmetrics.registerFontFamily('PTSans', normal='PTSans', bold='PTSans-Bold', italic='PTSans',
                                  boldItalic='PTSans-Bold')


def sections(text):
    pattern = r'^### L(\d+) Q(\d+) (.+?) — (\d+) marks?\n(.*?)(?=^## |^### |\Z)'
    return {(int(n), int(i)): (title, int(marks), body.strip())
            for n, i, title, marks, body in re.findall(pattern, text, re.M | re.S)}


def load_questions():
    prompts = sections((ROOT/'source/Student_questionnaire.md').read_text())
    answers = sections((ROOT/'source/Answer_key.md').read_text())
    expected = {(n, i) for n in TITLES for i in range(1, 11)}
    assert set(prompts) == set(answers) == expected, 'Question/answer IDs do not match'
    questions = []
    for (lecture, number), (title, points, body) in sorted(prompts.items()):
        key_title, key_points, guidance = answers[(lecture, number)]
        assert points == key_points
        options = re.findall(r'^- ([A-D])\. (.+)$', body, re.M)
        correct = re.fullmatch(r'Answer ([A-D])', key_title)
        assert [label for label, _ in options] == list('ABCD') and correct, f'L{lecture} Q{number}: require four choices and one correct answer'
        body = re.sub(r'^- [A-D]\. .+\n?', '', body, flags=re.M).strip()
        questions.append(dict(id=f'L{lecture} Q{number}', lecture=lecture, number=number,
            title=title, points=points, kind='multichoice',
            prompt_markdown=body, options=[dict(label=k, text=v) for k, v in options],
            correct_option=correct.group(1), grader_markdown=guidance))
    return questions


def add(doc, parent, name, text=None, **attrs):
    node = doc.createElement(name)
    for k, v in attrs.items():
        node.setAttribute(k, str(v))
    parent.appendChild(node)
    if text is not None:
        node.appendChild(doc.createTextNode(str(text)))
    return node


def rich(doc, parent, name, value):
    node = add(doc, parent, name, format='html')
    child = add(doc, node, 'text')
    assert ']]>' not in value
    child.appendChild(doc.createCDATASection(value))


def moodle_export(lecture, questions):
    doc = Document()
    quiz = add(doc, doc, 'quiz')
    category = add(doc, quiz, 'question', type='category')
    add(doc, add(doc, category, 'category'), 'text', f'$course$/ICA0024/Lecture {lecture:02}')
    for q in questions:
        node = add(doc, quiz, 'question', type=q['kind'])
        add(doc, add(doc, node, 'name'), 'text', f"{q['id']} {q['title']}")
        add(doc, node, 'idnumber', q['id'].replace(' ', '-'))
        rich(doc, node, 'questiontext', to_html(q['prompt_markdown']))
        rich(doc, node, 'generalfeedback', to_html(q['grader_markdown']))
        for key, value in [('defaultgrade', q['points']), ('penalty', 0), ('hidden', 0)]:
            add(doc, node, key, value)
        for key, value in [('single','true'), ('shuffleanswers','true'), ('answernumbering','ABCD')]:
            add(doc, node, key, value)
        for option in q['options']:
            answer = add(doc, node, 'answer', fraction=100 if option['label']==q['correct_option'] else 0, format='html')
            add(doc, answer, 'text').appendChild(doc.createCDATASection(to_html(option['text'])))
            rich(doc, answer, 'feedback', '')
        for tag in ['correctfeedback', 'partiallycorrectfeedback', 'incorrectfeedback']:
            rich(doc, node, tag, '')
        tags = add(doc, node, 'tags')
        question_tags = ['ICA0024', f'lecture-{lecture:02}', 'multiple-choice']
        if q['number'] >= 9:
            question_tags.append('practical-scenario')
        for tag in question_tags:
            add(doc, add(doc, tags, 'tag'), 'text', tag)
    path = ROOT/f'moodle/lecture-{lecture:02}.xml'
    path.write_bytes(doc.toprettyxml(indent='  ', encoding='UTF-8'))
    return path


def _page_decoration(canvas, doc):
    """Rose accent bar along the top edge; no running text, so Quick Import sees only the questions."""
    canvas.saveState()
    width, height = A4
    canvas.setFillColor(HexColor(XA['rose']))
    canvas.rect(0, height - 6, width, 6, stroke=0, fill=1)
    canvas.restoreState()


def forms_export(lecture, questions):
    register_fonts()
    path = ROOT/f'ms-forms/lecture-{lecture:02}.pdf'
    ink, navy, muted = HexColor(XA['ink']), HexColor(XA['navy']), HexColor(XA['muted'])
    styles = {
        'eyebrow': ParagraphStyle('eyebrow', fontName='PTSans-Bold', fontSize=8.5, leading=11, textColor=HexColor(XA['rose']),
                                  spaceAfter=4),
        'title': ParagraphStyle('title', fontName='PTSans-Bold', fontSize=22, leading=26, textColor=navy, spaceAfter=4),
        'subtitle': ParagraphStyle('subtitle', fontName='PTSans-Bold', fontSize=13, leading=17, textColor=HexColor(XA['slate']),
                                   spaceAfter=3),
        'meta': ParagraphStyle('meta', fontName='PTSans', fontSize=9.5, leading=13, textColor=muted, spaceAfter=10),
        'question': ParagraphStyle('question', fontName='PTSans-Bold', fontSize=12, leading=16, textColor=navy,
                                   spaceBefore=14, spaceAfter=6),
        'body': ParagraphStyle('body', fontName='PTSans', fontSize=10.5, leading=14.5, textColor=ink, spaceAfter=7),
        'option': ParagraphStyle('option', fontName='PTSans', fontSize=10.5, leading=14.5, textColor=ink,
                                 leftIndent=30, firstLineIndent=-16, spaceAfter=4),
        'code': ParagraphStyle('code', fontName='JetBrainsMono', fontSize=8, leading=10.5, textColor=navy,
                               spaceBefore=4, spaceAfter=9),
    }
    marks = sum(q['points'] for q in questions)
    story = [Paragraph('ICA0024 INFRASTRUCTURE AS CODE', styles['eyebrow']),
             Paragraph(f'ICA0024 Lecture {lecture}', styles['title']),
             Paragraph(inline(TITLES[lecture], 'JetBrainsMono'), styles['subtitle']),
             Paragraph(f'{len(questions)} questions, {marks} points. Choose one answer for each question.', styles['meta']),
             HRFlowable(width='100%', thickness=2, color=HexColor(XA['rose']), spaceBefore=2, spaceAfter=2)]
    for q in questions:
        if q['number'] in PAGE_BREAKS:
            story.append(PageBreak())
        elif q['number'] > 1:
            story.append(HRFlowable(width='100%', thickness=0.75, color=HexColor(XA['line']), spaceBefore=6, spaceAfter=0))
        block = []
        heading = inline(f"{q['number']}. {q['title']}", 'JetBrainsMono')
        number, _, rest = heading.partition(' ')
        points = f"({q['points']} {'point' if q['points'] == 1 else 'points'})"
        block.append(Paragraph(f'<font color="{XA["rose"]}">{number}</font> {rest} '
                               f'<font name="PTSans" color="{XA["muted"]}">{points}</font>', styles['question']))
        parts = re.split(r'(```[^\n]*\n.*?\n```)', q['prompt_markdown'], flags=re.S)
        for part in parts:
            if part.startswith('```'):
                code = part.split('\n', 1)[1].rsplit('\n```', 1)[0]
                block.append(Preformatted(ascii_text(code), styles['code']))
            else:
                for paragraph in re.split(r'\n\s*\n', part.strip()):
                    if not paragraph:
                        continue
                    paragraph = inline(paragraph, 'JetBrainsMono').replace('\n', '<br/>')
                    block.append(Paragraph(paragraph, styles['body']))
        for option in q['options']:
            text = inline(option['text'], 'JetBrainsMono')
            block.append(Paragraph(f'<font name="PTSans-Bold" color="{XA["navy"]}">{option["label"]}.</font> {text}',
                                   styles['option']))
        block.append(Spacer(1, 4))
        story.append(KeepTogether(block))
    SimpleDocTemplate(str(path), pagesize=A4, rightMargin=48, leftMargin=48,
                      topMargin=40, bottomMargin=36, title=f'ICA0024 Lecture {lecture}',
                      subject=TITLES[lecture], author='ICA0024', invariant=1).build(
                          story, onFirstPage=_page_decoration, onLaterPages=_page_decoration)
    return path


def self_check_export(questions):
    return self_check.build(questions, TITLES, ROOT/'assets/brand/logo-color.svg', SELF_CHECK)


def validate(questions, output_format='all'):
    report = {'questions':len(questions), 'total_marks':sum(q['points'] for q in questions),
              'moodle_live_import_tested':False, 'ms_forms_live_import_tested':False, 'lectures':[]}
    assert report['questions']==10*len(TITLES) and report['total_marks']==20*len(TITLES)
    assert all(q['kind']=='multichoice' for q in questions)
    if output_format in ('all', 'forms'):
        assert json.loads((ROOT/'ms-forms/grading-reference.json').read_text())==questions
    for lecture in TITLES:
        expected = [q for q in questions if q['lecture']==lecture]
        assert sum(q['points'] for q in expected)==20
        if output_format in ('all', 'moodle'):
            root = ET.parse(ROOT/f'moodle/lecture-{lecture:02}.xml').getroot()
            nodes = [q for q in root.findall('question') if q.get('type')!='category']
            assert len(nodes)==10
            for source, node in zip(expected,nodes):
                assert node.get('type')==source['kind']
                assert node.findtext('idnumber')==source['id'].replace(' ','-')
                assert float(node.findtext('defaultgrade'))==source['points']
                assert node.findtext('questiontext/text')==to_html(source['prompt_markdown'])
                # Round-trip comparison catches escaped YAML/HCL characters and whitespace damage.
                answers=node.findall('answer')
                assert len(answers)==4
                assert node.findtext('single')=='true'
                assert node.findtext('generalfeedback/text')==to_html(source['grader_markdown'])
                correct=[i for i,a in enumerate(answers) if a.get('fraction')=='100']
                assert correct==['ABCD'.index(source['correct_option'])]
                assert all(a.findtext('text')==to_html(o['text']) for a,o in zip(answers,source['options']))
        pdf_pages = None
        if output_format in ('all', 'forms'):
            pdf = ROOT/f'ms-forms/lecture-{lecture:02}.pdf'
            assert pdf.stat().st_size < 10_000_000
            reader=PdfReader(pdf)
            assert len(reader.pages) == len(PAGE_BREAKS) + 1, \
                f'Lecture {lecture}: a question overflowed its page; shorten it or adjust PAGE_BREAKS'
            text='\n'.join(p.extract_text() for p in reader.pages)
            normalized = re.sub(r'\s+', ' ', text)
            for q in expected:
                assert f"{q['number']}. {ascii_text(q['title'])}" in text
                for option in q['options']:
                    assert re.sub(r'\s+', ' ', ascii_text(f"{option['label']}. {option['text']}")) in normalized
                if q['kind']=='multichoice':
                    assert sum(all(ascii_text(option['text'])[:25] in page.extract_text() for option in q['options']) for page in reader.pages)==1, f"Split choices for {q['id']}"
            assert 'Instructor copy' not in text and 'Technical reference' not in text
            pdf_pages = len(reader.pages)
        report['lectures'].append(dict(lecture=lecture, questions=len(expected),
                                      multichoice=sum(q['kind']=='multichoice' for q in expected),
                                      essay=sum(q['kind']=='essay' for q in expected),
                                      marks=sum(q['points'] for q in expected), pdf_pages=pdf_pages))
    if output_format in ('all', 'selfcheck'):
        page = SELF_CHECK.read_text()
        report['self_check'] = self_check.validate(page, questions, TITLES)
    if output_format != 'all':
        report['validated_format'] = output_format
    return report


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--format', choices=['all', 'moodle', 'forms', 'selfcheck'], default='all',
                        help='Output format to generate or validate (default: all)')
    parser.add_argument('--check', action='store_true', help='Validate committed exports without rebuilding')
    args=parser.parse_args()
    questions=load_questions()
    if not args.check:
        if args.format in ('all', 'moodle'):
            (ROOT/'moodle').mkdir(exist_ok=True)
        if args.format in ('all', 'forms'):
            (ROOT/'ms-forms').mkdir(exist_ok=True)
        for lecture in TITLES:
            group=[q for q in questions if q['lecture']==lecture]
            if args.format in ('all', 'moodle'):
                moodle_export(lecture,group)
            if args.format in ('all', 'forms'):
                forms_export(lecture,group)
        if args.format in ('all', 'forms'):
            (ROOT/'ms-forms/grading-reference.json').write_text(json.dumps(questions,indent=2,ensure_ascii=False)+'\n')
        if args.format in ('all', 'selfcheck'):
            self_check_export(questions)
    report=validate(questions, args.format)
    # A partial build must not overwrite the complete validation report.
    if args.format == 'all':
        (ROOT/'docs/validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
