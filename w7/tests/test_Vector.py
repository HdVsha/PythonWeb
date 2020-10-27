import pytest
from my_mathematics.linear_algebra import Vector
import math
import numpy as np


@pytest.mark.parametrize("vector1, vector2", [([1, 2, 3], [2, 3, 5]), ([0, 0, 0], [0, 0, 0]), ([-1, -2, -3], [1, 2, 3]),
                                              ([100, 100, 0], [0, 4, 5]), ([0, 100, 100], [2, 34, 5]),
                                              ([-100, 0, 100], [1, 23, 4]), ([100, 0, 100], [0, 0, 0])])
def test_vector_nums(vector1, vector2):
    np_vector1 = np.array(vector1)
    np_vector2 = np.array(vector2)
    x = np.array([vector2, vector1])
    '''
    Have to convert to the same types in order to compare
    '''
    assert np_vector1.dot(np_vector2) == Vector(*vector1) * Vector(*vector2)  # No conversion to list bc they are numbers
    assert list(np.sum([np_vector1, np_vector2], axis=0)) == list(Vector(*vector1) + Vector(*vector2))
    # Conversion to array bc no other option is available
    assert np.diff(x, axis=0).any() == np.array(list(Vector(*vector1) - Vector(*vector2))).any()  # .any() bc arrays
    assert np.cross(np_vector1, np_vector2).tolist() == list(Vector(*vector1) & Vector(*vector2))


@pytest.mark.parametrize("vector1, vector2", [('1, 2, 3', '2, 3, 5'), ('0, 0, 0', '0, 0, 0'), ('-1, -2, -3', '1, 2, 3'),
                                              ('100, 100, 0', '0, 4, 5'), ('0, 100, 100', '2, 34, 5'),
                                              ('-100, 0, 100', '1, 23, 4'), ('100, 0, 100', '0, 0, 0')])
def test_vector_str(vector1, vector2):
    vector1 = list(map(float, list(vector1.split(','))))
    vector2 = list(map(float, list(vector2.split(','))))
    np_vector1 = np.array(vector1)
    np_vector2 = np.array(vector2)
    x = np.array([vector2, vector1])
    '''
    Have to convert to the same types in order to compare
    '''
    assert np_vector1.dot(np_vector2) == Vector(*vector1) * Vector(*vector2)  # No conversion to list bc they are numbers
    assert list(np.sum([np_vector1, np_vector2], axis=0)) == list(Vector(*vector1) + Vector(*vector2))
    # Conversion to array bc no other option is available
    assert np.diff(x, axis=0).any() == np.array(list(Vector(*vector1) - Vector(*vector2))).any()  # .any() bc arrays
    assert np.cross(np_vector1, np_vector2).tolist() == list(Vector(*vector1) & Vector(*vector2))

