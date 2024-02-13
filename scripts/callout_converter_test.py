import re

import pytest
from callout_converter import callout_pattern


def construct_callout(
        class_name: str='class_name', title: str='title', content: str='content 1\ncontent 2\n...\nlast line'):
    content = '> '+'\n> '.join(content.split('\n'))
    return f'''> [!{class_name}] {title}
{content}'''


def test_no_space_begining():
    callout = construct_callout()
    callout = '>'+callout[2:]
    match = re.search(callout_pattern, callout, flags=re.MULTILINE)
    assert match is not None


def test_brackets_in_title():
    title = 'This] [is] a [!title] with brackets]'
    example=f'''
content before

{construct_callout(title=title)}

content after'''
    match = re.search(callout_pattern, example, flags=re.MULTILINE)
    assert match is not None
    _, matched_title, _ = match[1], match[2], match[3]
    assert title == matched_title


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

