import pytest
from latex_converter import convert


def test_latex_converter():
    example = '''
$\\begin{pmatrix}
a & b \\\\
c & d
\\end{pmatrix}$
$$\\begin{pmatrix}
a & b \\\\
c & d
\\end{pmatrix}$$'''
    solution = '''
$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$

$$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$$
'''
    assert solution == convert(example)
