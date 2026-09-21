"""Export the editable concept glossary using the question build dependencies."""
import html
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate

from formatting import ascii_text, inline, to_html


def load_glossary(root):
    source = (root/'source/Glossary.md').read_text(encoding='utf-8')
    preamble, *parts = re.split(r'^## (Lecture [123]: .+)$', source, flags=re.M)
    title, intro = preamble.strip().split('\n', 1)
    assert title.startswith('# ') and intro.strip(), 'Glossary needs a title and introduction'
    sections, concepts = [], set()
    for heading, body in zip(parts[::2], parts[1::2]):
        entries = []
        assert not body.split('### ', 1)[0].strip(), 'Put definitions under term headings'
        for term, definition in re.findall(r'^### ([^\n]+)\n(.*?)(?=^### |\Z)', body, re.M | re.S):
            term, definition = term.strip(), definition.strip()
            assert term and definition, 'Empty glossary term or definition'
            assert term.casefold() not in concepts, f'Duplicate glossary term: {term}'
            assert not re.search(r'^#{1,6} ', definition, re.M), 'Unexpected heading in definition'
            concepts.add(term.casefold())
            entries.append((term, definition))
        assert entries, f'No terms under {heading}'
        sections.append((heading, sorted(entries, key=lambda entry: entry[0].casefold())))
    assert [heading.split(':')[0] for heading, _ in sections] == ['Lecture 1', 'Lecture 2', 'Lecture 3']
    return title[2:], intro.strip(), sections


def html_document(title, intro, sections):
    links = ' · '.join(f'<a href="#lecture-{i}">Lecture {i}</a>' for i in range(1, 4))
    body = [f'<h1>{html.escape(title)}</h1>', to_html(intro), f'<nav aria-label="Lectures">{links}</nav>']
    for i, (heading, entries) in enumerate(sections, 1):
        body.append(f'<section id="lecture-{i}"><h2>{html.escape(heading)}</h2><dl>')
        for term, definition in entries:
            body.append(f'<dt>{html.escape(term)}</dt><dd>{to_html(definition)}</dd>')
        body.append('</dl></section>')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
body {{ max-width: 52rem; margin: 2.5rem auto; padding: 0 1.5rem; font: 17px/1.55 Arial, sans-serif; color: #253348; }}
h1 {{ font-size: 2rem; line-height: 1.2; }}
h2 {{ margin-top: 2.5rem; padding-bottom: .4rem; border-bottom: 1px solid #ccd4df; font-size: 1.4rem; }}
nav {{ margin: 1.5rem 0; }} a {{ color: #1d527e; }}
dt {{ font-weight: bold; margin-top: 1.2rem; break-after: avoid; }}
dd {{ margin: .25rem 0 0; }} dd p {{ margin: 0 0 .6rem; }}
@media print {{ body {{ max-width: none; margin: 0; font-size: 11pt; }} nav {{ display: none; }} }}
</style></head><body><main>{''.join(body)}</main></body></html>
'''


def moodle_document(title, intro, sections):
    root = ET.Element('GLOSSARY')
    info = ET.SubElement(root, 'INFO')
    settings = {'NAME': title, 'INTRO': to_html(intro), 'INTROFORMAT': 1,
                'ALLOWDUPLICATEDENTRIES': 0, 'DISPLAYFORMAT': 'dictionary',
                'SHOWSPECIAL': 1, 'SHOWALPHABET': 1, 'SHOWALL': 1,
                'ALLOWCOMMENTS': 0, 'USEDYNALINK': 0, 'DEFAULTAPPROVAL': 1,
                'GLOBALGLOSSARY': 0, 'ENTBYPAGE': 20}
    for tag, value in settings.items():
        ET.SubElement(info, tag).text = str(value)
    nodes = ET.SubElement(info, 'ENTRIES')
    for heading, entries in sections:
        for term, definition in entries:
            entry = ET.SubElement(nodes, 'ENTRY')
            fields = {'CONCEPT': term, 'DEFINITION': to_html(definition), 'FORMAT': 1,
                      'DEFINITIONTRUST': 0, 'USEDYNALINK': 0, 'CASESENSITIVE': 0,
                      'FULLMATCH': 1, 'TEACHERENTRY': 1}
            for tag, value in fields.items():
                ET.SubElement(entry, tag).text = str(value)
            category = ET.SubElement(ET.SubElement(entry, 'CATEGORIES'), 'CATEGORY')
            ET.SubElement(category, 'NAME').text = heading
            ET.SubElement(category, 'USEDYNALINK').text = '0'
    ET.indent(root, space='  ')
    return ET.tostring(root, encoding='utf-8', xml_declaration=True) + b'\n'


def pdf_document(path, title, intro, sections):
    ink = colors.HexColor('#253348')
    styles = {
        'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=20, leading=25, textColor=ink, spaceAfter=12),
        'heading': ParagraphStyle('heading', fontName='Helvetica-Bold', fontSize=14, leading=19, textColor=ink, spaceAfter=14, keepWithNext=True),
        'term': ParagraphStyle('term', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=ink, spaceBefore=8, spaceAfter=3),
        'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10.5, leading=14.5, spaceAfter=8),
    }
    story = [Paragraph(inline(title), styles['title']), Paragraph(inline(intro), styles['body'])]
    for i, (heading, entries) in enumerate(sections):
        if i:
            story.append(PageBreak())
        story.append(Paragraph(inline(heading), styles['heading']))
        for term, definition in entries:
            paragraphs = [Paragraph(inline(term), styles['term'])]
            paragraphs += [Paragraph(inline(p).replace('\n', '<br/>'), styles['body'])
                           for p in re.split(r'\n\s*\n', definition)]
            story.append(KeepTogether(paragraphs))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(ink)
        canvas.drawString(40, 24, 'ICA0024 | Concept glossary | Lectures 1-3')
        canvas.drawRightString(A4[0]-40, 24, str(doc.page))
        canvas.restoreState()

    SimpleDocTemplate(str(path), pagesize=A4, leftMargin=40, rightMargin=40,
                      topMargin=36, bottomMargin=42, title=title, author='ICA0024',
                      invariant=1).build(story, onFirstPage=footer, onLaterPages=footer)


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def normalized_text(value):
    parser = PlainText()
    parser.feed(to_html(value))
    return ' '.join(ascii_text(' '.join(parser.parts)).split())


def build_glossary(root, check=False):
    title, intro, sections = load_glossary(root)
    output = root/'glossary'
    expected_html = html_document(title, intro, sections)
    expected_xml = moodle_document(title, intro, sections)
    if not check:
        output.mkdir(exist_ok=True)
        (output/'glossary.html').write_text(expected_html, encoding='utf-8')
        (output/'moodle-glossary.xml').write_bytes(expected_xml)
        pdf_document(output/'glossary.pdf', title, intro, sections)
    assert (output/'glossary.html').read_text(encoding='utf-8') == expected_html, 'Stale glossary HTML'
    assert (output/'moodle-glossary.xml').read_bytes() == expected_xml, 'Stale glossary XML'
    entries = [(heading, term, definition) for heading, group in sections for term, definition in group]
    nodes = ET.parse(output/'moodle-glossary.xml').findall('./INFO/ENTRIES/ENTRY')
    assert len(nodes) == len(entries)
    for (heading, term, definition), node in zip(entries, nodes):
        assert node.findtext('CONCEPT') == term
        assert node.findtext('DEFINITION') == to_html(definition)
        assert node.findtext('CATEGORIES/CATEGORY/NAME') == heading
        assert node.findtext('FORMAT') == '1'
    reader = PdfReader(output/'glossary.pdf')
    text = ' '.join(' '.join(page.extract_text().split()) for page in reader.pages)
    for _, term, definition in entries:
        assert normalized_text(term) in text, f'Missing PDF term: {term}'
        assert normalized_text(definition) in text, f'Stale or missing PDF definition: {term}'
    return {'terms': len(entries), 'lectures': len(sections), 'pdf_pages': len(reader.pages),
            'moodle_live_import_tested': False}
