import random
import pytest
from calculate.operators import Operators


def test_multiple_multiplication():
    op = Operators()
    assert op.multiplication("10000 * 1000 * 100 * 10 * 1") == 10000000000


def test_random_multiplication():
    op = Operators()
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    operation = f'{n1} * {n2}'
    result = n1 * n2
    assert op.multiplication(operation) == result


def test_invalid_multiplication():
    op = Operators()
    with pytest.raises(TypeError):
        op.multiplication(2)