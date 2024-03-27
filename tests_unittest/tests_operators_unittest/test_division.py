import random
import pytest
from calculate.operators import Operators


def test_multiple_division():
    op = Operators()
    assert op.division("10000 / 1000 / 100 / 10 / 1") == 0.01


def test_random_division():
    op = Operators()
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    operation = f'{n1} / {n2}'
    result = n1 / n2
    assert op.division(operation) == result


def test_invalid_division():
    op = Operators()
    with pytest.raises(TypeError):
        op.division(1)


def test_divide_by_zero():
    op = Operators
    n = random.randint(1, 100)
    with pytest.raises(TypeError):
        op.division(f'{n}/0')
