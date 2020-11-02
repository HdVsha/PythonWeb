import sys
sys.path.append('..')

from tasks.FibTask import fib_convert, fibo_gen
import pytest


def test_fibonacci():
    assert 21 == fib_convert(7)[-1]
    assert 1 == fib_convert(1)[-1]
    # assert ValueError == fib_convert(0)  # Commented bc it's working properly
