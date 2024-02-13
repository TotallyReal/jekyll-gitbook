import re


callout_pattern = r'^>\s?\[!(.*?)\]([-|+]?) (.*?)\n([\s\S]*?)(?=(\n[^>])|\Z)'


def convert_content(content: str) -> str:
    """
    Converts the content from the markdown quote syntax to plain text.
    """
    return '\n\n'.join(line[1:].lstrip() for line in content.split('\n'))


def process_match(match):
    class_name, collapsible_type, title, content = match[1], match[2], match[3], match[4]
    collapsible_title = 'collapsible' if len(collapsible_type)>0 else ''
    collapsible_content = 'data-collapsed' if collapsible_type=='-' else ''
    content = convert_content(content)
    return f'''
{{::options parse_block_html="true" /}}
<div class="callout" data-callout="{class_name}">

  {{::options parse_block_html="false" /}}
  <div class="callout-title" {collapsible_title}>{title}</div>
  {{::options parse_block_html="true" /}}
  <div class="callout-content-wrapper" {collapsible_content}>
  <div class="callout-content">
{content}
  </div>
  </div>
</div>
{{::options parse_block_html="false" /}}'''


def convert(text):
    return re.sub(callout_pattern, process_match, text, flags=re.MULTILINE)
