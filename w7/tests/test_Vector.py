import pytest
from my_mathematics.linear_algebra import Vector
import math
import numpy as np


@pytest.mark.parametrize("vector1, vector2", [([1, 2, 3], [2,3,5]), ([0, 0, 0],[0, 0, 0]), ([-1, -2, -3], [1, 2, 3]),
                                    ([100, 100, 0], [0,4,5]), ([0, 100, 100], [2, 34, 5]),
                                    ([-100, 0, 100], [1, 23, 4]),([100, 0, 100], [0, 0, 0])])
def test_vector(vector1, vector2):
    np_vector1 = np.array(vector1)
    np_vector2 = np.array(vector2)
