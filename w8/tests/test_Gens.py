import sys
sys.path.append('..')

from tasks.FibTask import fibonacci
import pytest


def test_fibonacci():
    assert 21 == fibonacci(7)
    assert 1 == fibonacci(1)
    assert ValueError == fibonacci(0)
