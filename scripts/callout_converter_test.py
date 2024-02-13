import re

import pytest
from callout_converter import callout_pattern, convert_content


def construct_callout(
        class_name: str='class_name', title: str='title', content: str='content 1\ncontent 2\n...\nlast line'):
    content = '> '+'\n> '.join(content.split('\n'))
    return f'''> [!{class_name}] {title}
{content}'''


def test_no_space_begining_title():
    callout = construct_callout()
    callout = '>'+callout[2:]
    match = re.search(callout_pattern, callout, flags=re.MULTILINE)
    assert match is not None


def test_no_space_begining_content():
    assert convert_content('> line1\n>line2\n>    line3')=='line1\n\nline2\n\nline3'


def test_brackets_in_title():
    title = 'This] [is] a [!title] with brackets]'
    example=f'''
content before

{construct_callout(title=title)}

content after'''
    match = re.search(callout_pattern, example, flags=re.MULTILINE)
    assert match is not None
    assert title == match[3]


def test_finish_callout_by_string_end():
    example = f'''
content before

{construct_callout()}'''
    match = re.search(callout_pattern, example, flags=re.MULTILINE)
    assert match is not None


def test_finish_with_empty_line_with_spaces():
    example = f'''
content before

{construct_callout()}
     '''
    match = re.search(callout_pattern, example, flags=re.MULTILINE)
    assert match is not None


def test_finish_with_nonquote_line():
    example = f'''
content before

{construct_callout()}
This is a line'''
    match = re.search(callout_pattern, example, flags=re.MULTILINE)
    assert match is not None

