import sys
import base64
import callout_converter
import latex_converter

# Retrieve the value of s from command-line arguments
input = base64.b64decode(sys.argv[1]).decode('utf-8')

# print(f'input: \n{input}')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# print(f'output:')
print(latex_converter.convert(callout_converter.convert(input)))