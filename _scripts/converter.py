import sys
import base64
import callout_converter
import latex_converter
import wikilinks_converter

# Retrieve the value of s from command-line arguments
input = base64.b64decode(sys.argv[1]).decode('utf-8')

converters = [
    callout_converter,
    latex_converter,
    wikilinks_converter
]

# print(f'input: \n{input}')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'output:')
output = input
for converter in converters:
    output = converter.convert(output)
print(output)
