"""Shared Markdown formatting for course materials."""
import markdown


def to_html(value):
    return markdown.markdown(value, extensions=['fenced_code', 'sane_lists'])
