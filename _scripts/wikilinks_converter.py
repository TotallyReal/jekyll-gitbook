import os
import os.path
from typing import List
import re
from dataclasses import dataclass

# TODO: change to be parameters from _config.yml
base_dir = 'C:/gem/myblog/notes'
link_base_dir = '\\Fourier_Notes\\notes'

# TODO: support links with directory in it


@dataclass
class Link:

    embed: bool
    filename: str
    caption: str

    @staticmethod
    def from_match(match: re.Match):
        return Link(embed=(match[1] == '!'), filename=match[2], caption=match[5])

    def to_wikilink(self):
        caption_str = '' if self.caption is None else f'|{self.caption}'
        embed_str = '!' if self.embed else ''
        return f'{embed_str}[[{self.filename}{caption_str}]]'


def process_match(match):
    global file_dict
    link = Link.from_match(match)
    if link.filename not in file_dict:
        return f'{link.embed}[[invalid wikilink: {link.filename}]]'

    if not link.embed:
        caption = link.filename if link.caption is None else link.caption
        return f'<a href="{file_dict[link.filename]}">{caption}</a>'

    only_file_name, file_extension = link.filename.split('.', 1)

    if file_extension.lower() in ['png', 'jpg', 'jpeg', 'gif']:
        width = f'width={link.caption}' if (link.caption and link.caption.isdigit()) else ''
        return f'<img src="{file_dict[link.filename]}" {width}>'

    return f'{link.embed}[[invalid wikilink: {link.filename}]]'


def create_file_dict(base_dir: str, link_base_dir: str, ignore_dirs: List[str]):
    file_dict = {}

    for dirpath, dirnames, filenames in os.walk(base_dir):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for filename in filenames:
            if filename[-3:] == '.md':
                filename = filename[:-3]
            file_dict[filename] = f'{dirpath.replace(base_dir, link_base_dir)}/{filename}'
    return file_dict


wikilink_regex = r'(!)?\[\[(.*?)((\||\\\|)(.*?))?\]\]'


subfolders = [d for d in os.listdir(base_dir)
              if os.path.isdir(os.path.join(base_dir, d)) and d[0] == '_']
file_dict = {}
for subfolder in subfolders:
    file_dict.update(create_file_dict(
        base_dir=os.path.join(base_dir, subfolder),
        link_base_dir=f'{link_base_dir}\\{subfolder[1:]}',
        ignore_dirs=['.obsidian']))


def convert(text):
    output = re.sub(wikilink_regex, process_match, text, flags=re.MULTILINE)
    return output # +'\n'+str(file_dict)

