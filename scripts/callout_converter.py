import re


callout_pattern = r'^>\s?\[!(.*?)\][-|+]? (.*?)\n([\s\S]*?)(?=(\n[^>])|\Z)'


def process_match(match):
    class_name, title, content = match[1], match[2], match[3]
    content = '\n\n'.join(line[2:] for line in content.split('\n'))
    return f'''
{{::options parse_block_html="true" /}}
<div class="callout" data-callout="{class_name}">

  {{::options parse_block_html="false" /}}
  <div class="env-title">{title}</div>
  {{::options parse_block_html="true" /}}
  
  <div class="env-content">
{content}
  </div>
</div>
{{::options parse_block_html="false" /}}'''


def convert(text):
    return re.sub(callout_pattern, process_match, text, flags=re.MULTILINE)
