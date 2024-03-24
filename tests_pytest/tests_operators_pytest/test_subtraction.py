import pytest
import random
from calculate.operators import Operators


def test_multiple_subtraction():
    op = Operators()
    assert op.subtraction('1 - 8 - 7 - 9 - 4 - 3') == -30


def test_random_subtraction():
    op = Operators()
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    operation = f'{n1} - {n2}'
    result = n1 - n2
    assert op.subtraction(operation) == result


def test_invalid_subtraction():
    op = Operators()
    with pytest.raises(TypeError):
        op.subtraction(3)