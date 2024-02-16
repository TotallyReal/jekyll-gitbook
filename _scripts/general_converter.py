import sys
import os
from log_system import create_logger, clear_file
import base64
import callout_converter
import latex_converter
import wikilinks_converter

logger = create_logger(__file__)
clear_file(logger)

text = base64.b64decode(sys.argv[1]).decode('utf-8')

converters = [
    callout_converter,
    latex_converter,
    wikilinks_converter
]
output = text
for converter in converters:
    output = converter.convert(output)

sys.stdout.buffer.write(output.encode('utf-8'))

