import re

display_latex_pattern = r'\$\$([\s\S]*?)\$\$'
inline_latex_pattern = r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)'


br_open = "{::nomarkdown}"
br_close = "{:/}"


def no_double_no_markdown(text: str):
    # Create a regular expression pattern to match either delimiter1 or delimiter2
    pattern = f"({br_open}|{br_close})"

    # Split the text using the pattern
    parts = re.split(pattern, text)

    # Filter out empty strings and None elements
    parts = [part for part in parts if part]

    open_counter = 0
    for i in range(len(parts)):
        if parts[i] == br_open:
            open_counter += 1
            if open_counter > 1:
                parts[i] = ''
            continue

        if parts[i] == br_close:
            open_counter -= 1
            if open_counter >= 1:
                parts[i] = ''
            if open_counter < 0:
                raise Exception('no markdown brackets are not balanced')

    if open_counter > 0:
        raise Exception('no markdown brackets are not balanced')

    return ''.join(parts)


def no_open_html_tag(latex_str: str):
    return re.sub('<', lambda match: '< ', latex_str)


def no_markdown(latex_str: str):
    return f'{{::nomarkdown}} <span> {latex_str} </span> {{:/}}'


def process_match_display(match: re.Match):
    latex_str = match[0]
    latex_str = latex_str.replace('\n', ' ')
    latex_str = no_open_html_tag(latex_str)
    return no_markdown('\n'+latex_str+'\n')


def process_match_inline(match: re.Match):
    latex_str = match[0]
    latex_str = latex_str.replace('\n', ' ')
    latex_str = no_open_html_tag(latex_str)
    return no_markdown(latex_str)
    # return no_markdown(f'$\n{latex_str[1:]}')


def convert(text: str):
    text = re.sub(display_latex_pattern, process_match_display, text, flags=re.MULTILINE)
    # Note that inline formula will also find the double dollar signs $$ in the display formulas.
    # However, since there is nothing between them, and we just remove new lines, it doesn't really matter
    return no_double_no_markdown(re.sub(inline_latex_pattern, process_match_inline, text, flags=re.MULTILINE))


