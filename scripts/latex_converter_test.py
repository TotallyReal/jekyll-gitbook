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


def test_me():
    example = r'''$$\align{\int_c^d f(t) \dt &= \frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\pi\chi_{[c,d]}\dt = \angles{f,\pi\chi_{[c,d]}} \\ & =\angles{\frac{a_0}{2} + \sum_1^\infty (a_n \cos(nx)+ b_n\sin(nx)),\pi\chi_{[c,d]}}.}$$

Using the fact that the inner product is continuous (with respect to the $\norm{\cdot}_2$ norm), we can take the summation outside the integral to obtain:

$$\align{\int_c^d f(t) \dt &=\angles{\frac{a_0}{2}, \pi\chi_{[c,d]}} + \sum_1^\infty\angles{a_n \cos(nx)+ b_n\sin(nx),\pi\chi_{[c,d]}} \\ & = \int_c^d\frac{a_0}{2} \dt + \sum_1^\infty\int_c^d(a_n \cos(nx)+ b_n\sin(nx))\dt \\ & = \frac{a_0(d-c)}{2} \dt + \sum_1^\infty(\frac{a_n}{n} (\sin(nd)-\sin(bc))- \frac{b_n}{n}(\cos(nd)-\cos(nc))\dt.}$$'''
    solution = convert(example)
    print(solution)
    assert False