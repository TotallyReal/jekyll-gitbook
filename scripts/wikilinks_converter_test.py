import pytest
import re
from wikilinks_converter import convert, wikilink_regex, Link


@pytest.mark.parametrize("embed", [False, True])
@pytest.mark.parametrize("file_name", ['file_name', 'file_name.ext'])
@pytest.mark.parametrize("caption", [None, ' This is a caption', 'This is a caption'])
def test_regex(embed: bool, file_name: str, caption: str):
    caption_str = '' if caption is None else f'|{caption}'
    embed_str = '' if embed is None else embed
    link = Link(embed=embed, filename=file_name, caption=caption)
    example=f'''before    
inline {link.to_wikilink()} after inline
after'''
    match = re.search(pattern=wikilink_regex,string=example)
    assert match is not None

    link_from_match = Link.from_match(match)
    assert link_from_match == link
