from tasks.FibTask import fibonacci
import pytest


@pytest.mark.parametrize('num', [1, 5, 7])
def test_fibonacci(num):
    assert 21 == fibonacci(7)
    assert 1 == fibonacci(1)