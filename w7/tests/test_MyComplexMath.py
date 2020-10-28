import pytest, math, cmath
from my_mathematics.Complex import Complex
import numpy as np


@pytest.mark.parametrize("num1, num2", [[(-2, 1), (15, -50)], [(1, -2), (3, 50)], [(1, 2), (10, 50)], [(0, 0), (1, 3)]])
def test_complex(num1, num2):
    #  [0] - real part, [1] - imag part
    a = Complex(num1[0], num1[1])
    b = Complex(num2[0], num2[1])
    z1 = complex(num1[0], num1[1])
    z2 = complex(num2[0], num2[1])
    assert z1 + z2 == a + b
    assert z1 - z2 == a - b
    assert z1 ** 5 == a ** 5
    assert z2 ** (1/2) == b ** (1/2)
    assert z1 * z2 == a * b
    assert z1 / z2 == a / b
    assert z2 / z1 == b / a
    assert abs(z1) == a.abs()
    assert abs(z2) == b.abs()
