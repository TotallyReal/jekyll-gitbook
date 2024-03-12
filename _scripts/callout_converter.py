import re
import logging
import os
from dataclasses import dataclass


@dataclass
class Callout:

    class_name: str
    title: str
    collapsible: str
    content: str

    @staticmethod
    def from_match(match: re.Match) -> 'Callout':
        return Callout(class_name=match[1], collapsible=match[2], title=match[3], content=convert_content(match[4]))

    def to_html(self):
        collapsible_attr = ''
        if len(self.collapsible)>0:
            collapsible_state = 'hide' if self.collapsible == '-' else 'show'
            collapsible_attr = f'collapsible="{collapsible_state}"'
        content = convert_content(self.content)

        return f'''
{{::options parse_block_html="true" /}}
<div class="callout" data-callout="{self.class_name}" {collapsible_attr}>

  {{::nomarkdown}}
  <div class="callout-title">{self.title}</div>
  {{:/}}
  <div class="callout-content-wrapper">
  <div class="callout-content">
{content}
  </div>
  </div>
</div>
{{::options parse_block_html="false" /}}'''



callout_pattern = r'^>\s?\[!(.*?)\]([-|+]?)[ \t]*(\S.*?)\n((?:[ \t]*>.*(?:\n|$))+)'

# callout_pattern = r'^>\s?\[!(.*?)\]([-|+]?) (.*?)\n([\s\S]*?)(?=(\n[^>])|\Z)'


def convert_content(content: str) -> str:
    """
    Converts the content from the markdown quote syntax to plain text.
    """
    return '\n\n'.join(line.lstrip()[1:] for line in content.split('\n'))


def process_match(match):
    class_name, collapsible_type, title, content = match[1], match[2], match[3], match[4]
    collapsible_attr = ''
    if len(collapsible_type)>0:
        collapsible_state = 'hide' if collapsible_type == '-' else 'show'
        collapsible_attr = f'collapsible="{collapsible_state}"'
    content = convert_content(content)

    return f'''
{{::options parse_block_html="true" /}}
<div class="callout" data-callout="{class_name}" {collapsible_attr}>

  {{::nomarkdown}}
  <div class="callout-title">{title}</div>
  {{:/}}
  <div class="callout-content-wrapper">
  <div class="callout-content">
{content}
  </div>
  </div>
</div>
{{::options parse_block_html="false" /}}'''


def convert(text: str):
    # if text.startswith('LOG'):
    #     with open(log_file, 'w'):
    #         pass
    #     logging.info('\n\n---------------------------\nConverting the text: ')
    #     logging.info(text)
    return re.sub(callout_pattern, process_match, text, flags=re.MULTILINE)
