import unittest
import random
from calculate.operators import Operators


class TestAddition(unittest.TestCase):
    def test_multiple_addition(self):
        op = Operators()
        self.assertEqual(op.addition("5.5 + 10 + 30 + 13.7 + 0.8"), 60)

    def test_random_addition(self):
        op = Operators()
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        operation = f'{n1} + {n2}'
        result = n1 + n2
        self.assertEqual(op.addition(operation), result)


if __name__ == "__main__":
    unittest.main()