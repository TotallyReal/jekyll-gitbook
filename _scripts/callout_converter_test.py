import re

import pytest
from callout_converter import callout_pattern, convert_content, convert, Callout


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


def test_lots_of_space_before_title():
    title = '                Only now title'
    example=f'''
content before

{construct_callout(title=title)}

content after'''
    match = re.search(callout_pattern, example, flags=re.MULTILINE)
    assert match is not None
    assert 'Only now title' == Callout.from_match(match).title


# def test_no_space_begining_content():
#     assert convert_content('> line1\n>line2\n>    line3')=='line1\n\nline2\n\nline3'


def test_brackets_in_title():
    title = 'This] [is] a [!title] with brackets]'
    example=f'''
content before

{construct_callout(title=title)}

content after'''
    match = re.search(callout_pattern, example, flags=re.MULTILINE)
    assert match is not None
    assert title == Callout.from_match(match).title


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


def test_hebrew_callout():
    example='''> [!משפט] משפט דיריכלה
> יש
הרבה
ראשונייים.'''
    match = re.search(callout_pattern, example, flags=re.MULTILINE)
    assert match is not None


def test_space_between_callouts():
    # Should be able to separate between different callouts
    example='''
>[!def] Definition: 
 > content



>[!remark] Remark:
 > content
 '''
    matches = re.findall(callout_pattern, example, flags=re.MULTILINE)
    assert len(matches) == 2


def test_me():
    example=r'''


> [!הערה]- הערה: 
> במקרה של פולינומים (מעל $\CC$) קיבלנו ממש את השוויון $f(x)=\sum_0^d a_kx^k$ לכל $x$. כפי שכבר ראינו, במקרה של טורי והתמרות פורייה, צריך לעבוד קצת יותר בשביל השוויון הזה.

 '''
    print('\n')
    print('matches')
    for match in re.findall(callout_pattern, example, flags=re.MULTILINE):
        print('%')
        # print(Callout.from_match(match))
    print('end')

    result = convert(example)
    print(result)
    assert result is None

