import re

display_latex_pattern = r'\$\$([\s\S]*?)\$\$'
inline_latex_pattern = r'\$([\s\S]*?)\$'


def process_match_display(match: str):
    return '\n'+match[0].replace('\n', ' ')+'\n'


def process_match_inline(match: str):
    return match[0].replace('\n', ' ')


def convert(text):
    text = re.sub(display_latex_pattern, process_match_display, text, flags=re.MULTILINE)
    # Note that inline formula will also find the double dollar signs $$ in the display formulas.
    # However, since there is nothing between them, and we just remove new lines, it doesn't really matter
    return re.sub(inline_latex_pattern, process_match_inline, text, flags=re.MULTILINE)
