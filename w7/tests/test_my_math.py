import pytest
from my_mathematics.math import MyMath
import math


@pytest.mark.parametrize("value", [0, 1, 90, -1, -90, 1000, 40, 50])
def test_math_lib(value):
    assert MyMath.sin(value) == math.sin(value)
