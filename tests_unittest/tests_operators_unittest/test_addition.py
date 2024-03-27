import random
import pytest
from calculate.operators import Operators


def test_multiple_addition():
    op = Operators()
    assert op.addition("5.5 + 10 + 30 + 13.7 + 0.8") == 60


def test_random_addition():
    op = Operators()
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    operation = f'{n1} + {n2}'
    result = n1 + n2
    assert op.addition(operation) == result


def test_invalid_addition():
    op = Operators()
    with pytest.raises(TypeError):
        op.addition(4)