"""Shared Markdown and PDF text formatting for course materials."""
import html
import re

import markdown


def to_html(value):
    return markdown.markdown(value, extensions=['fenced_code', 'sane_lists'])


def ascii_text(value):
    return value.translate(str.maketrans({'—':'-', '–':'-', '−':'-', '“':'"', '”':'"', '’':"'", '‘':"'", '\u00a0':' '}))


def inline(value, mono='Courier'):
    value = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', value)
    value = html.escape(ascii_text(value))
    value = re.sub(r'`([^`]+)`', rf'<font name="{mono}">\1</font>', value)
    return re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', value)
