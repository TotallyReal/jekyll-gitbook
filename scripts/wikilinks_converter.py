import os
import os.path
from typing import List
import re


def process_match(match):
    global file_dict
    embed, filename, caption = match[1], match[2], match[4]
    if filename not in file_dict:
        return f'{embed}[[invalid wikilink: {filename}]]'

    if embed is None:
        caption = filename if caption is None else caption
        return f'<a href="{file_dict[filename]}">{caption}</a>'

    only_file_name, file_extension = filename.split('.', 1)
    if file_extension.lower() in ['png', 'jpg', 'jpeg']:
        width = f'width={caption}' if caption.isdigit() else ''
        return f'<img src="{file_dict[filename]}" {width}>'

    return f'{embed}[[invalid wikilink: {filename}]]'


def create_file_dict(base_dir: str, link_base_dir: str, ignore_dirs: List[str]):
    file_dict = {}
    base_dir = 'C:/gem/myblog/_pages' # TODO - extract this directory automatically

    for dirpath, dirnames, filenames in os.walk(base_dir):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for filename in filenames:
            if filename[-3:] == '.md':
                filename = filename[:-3]
            file_dict[filename] = f'{dirpath.replace(base_dir, link_base_dir)}\{filename}'
    return file_dict


wikilink_regex = r'(!)?\[\[(.*?)(\|(.*?))?\]\]'


file_dict = create_file_dict(base_dir='..\_pages', link_base_dir='\Fourier_Notes\pages', ignore_dirs=['.obsidian'])


def convert(text):
    output = re.sub(wikilink_regex, process_match, text, flags=re.MULTILINE)
    return output # +'\n'+str(file_dict)


example='''---
title: Course Description
author: Ofir David
category: Fourier Analysis
layout: post
---
[[Fourier_Series]]
![[imgimg.png]]
before content 
'''



# for match in re.findall(pattern=wikilink_regex, string=example):
#     print(match)

# print(convert(example))

# for key, value in file_dict.items():
#     print(f'{key}: {value}')