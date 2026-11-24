#!/usr/bin/env python3
"""Compile the reviewed Markdown questions into Moodle XML, the question data file, and the self-check page."""
import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.dom.minidom import Document

import self_check
from formatting import to_html

ROOT = Path(__file__).resolve().parents[1]
TITLES = {1: 'Infrastructure as Code concepts', 2: 'Images and machine initialization',
          3: 'Server state and configuration organization',
          4: 'Resilience and verifying configuration code',
          5: 'Declarative cloud provisioning and state',
          6: 'Choosing cloud deployment options',
          7: 'Modules, testing, and automated quality checks',
          8: 'Module versioning and interface design',
          9: 'GitOps, pipelines, and team workflows'}

# Questions and marks per lecture; Lecture 9 lost its release-versus-deploy question.
COUNTS = {n: 10 for n in TITLES} | {9: 9}
MARKS = {n: 20 for n in TITLES} | {9: 18}

SELF_CHECK = ROOT/'self-check/index.html'
QUESTIONS_JSON = ROOT/'data/questions.json'


def sections(text):
    pattern = r'^### L(\d+) Q(\d+) (.+?) — (\d+) marks?\n(.*?)(?=^## |^### |\Z)'
    return {(int(n), int(i)): (title, int(marks), body.strip())
            for n, i, title, marks, body in re.findall(pattern, text, re.M | re.S)}


def load_questions():
    prompts = sections((ROOT/'source/Student_questionnaire.md').read_text())
    answers = sections((ROOT/'source/Answer_key.md').read_text())
    expected = {(n, i) for n in TITLES for i in range(1, COUNTS[n] + 1)}
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


def self_check_export(questions):
    return self_check.build(questions, TITLES, ROOT/'assets/brand/logo-color.svg', SELF_CHECK)


def validate(questions, output_format='all'):
    report = {'questions':len(questions), 'total_marks':sum(q['points'] for q in questions),
              'moodle_live_import_tested':False, 'lectures':[]}
    assert report['questions']==sum(COUNTS.values()) and report['total_marks']==sum(MARKS.values())
    assert all(q['kind']=='multichoice' for q in questions)
    if output_format in ('all', 'selfcheck'):
        assert json.loads(QUESTIONS_JSON.read_text())==questions
    for lecture in TITLES:
        expected = [q for q in questions if q['lecture']==lecture]
        assert len(expected)==COUNTS[lecture] and sum(q['points'] for q in expected)==MARKS[lecture]
        if output_format in ('all', 'moodle'):
            root = ET.parse(ROOT/f'moodle/lecture-{lecture:02}.xml').getroot()
            nodes = [q for q in root.findall('question') if q.get('type')!='category']
            assert len(nodes)==COUNTS[lecture]
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
        report['lectures'].append(dict(lecture=lecture, questions=len(expected),
                                      multichoice=sum(q['kind']=='multichoice' for q in expected),
                                      essay=sum(q['kind']=='essay' for q in expected),
                                      marks=sum(q['points'] for q in expected)))
    if output_format in ('all', 'selfcheck'):
        page = SELF_CHECK.read_text()
        report['self_check'] = self_check.validate(page, questions, TITLES)
    if output_format != 'all':
        report['validated_format'] = output_format
    return report


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--format', choices=['all', 'moodle', 'selfcheck'], default='all',
                        help='Output format to generate or validate (default: all)')
    parser.add_argument('--check', action='store_true', help='Validate committed exports without rebuilding')
    args=parser.parse_args()
    questions=load_questions()
    if not args.check:
        if args.format in ('all', 'moodle'):
            (ROOT/'moodle').mkdir(exist_ok=True)
        for lecture in TITLES:
            group=[q for q in questions if q['lecture']==lecture]
            if args.format in ('all', 'moodle'):
                moodle_export(lecture,group)
        if args.format in ('all', 'selfcheck'):
            QUESTIONS_JSON.parent.mkdir(exist_ok=True)
            QUESTIONS_JSON.write_text(json.dumps(questions,indent=2,ensure_ascii=False)+'\n')
        if args.format in ('all', 'selfcheck'):
            self_check_export(questions)
    report=validate(questions, args.format)
    # A partial build must not overwrite the complete validation report.
    if args.format == 'all':
        (ROOT/'docs/validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
