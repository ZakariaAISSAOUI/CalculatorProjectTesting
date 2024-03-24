import unittest
import random
from calculate.operators import Operators


class TestAddition(unittest.TestCase):
    def setUp(self):
        self.op = Operators()

    def test_multiple_addition(self):
        self.assertEqual(self.op.addition("5.5 + 10 + 30 + 13.7 + 0.8"), 60)

    def test_random_addition(self):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        self.assertEqual(self.op.addition(f'{n1} + {n2}'), n1 + n2)

    def test_invalid_addition(self):
        with self.assertRaises(TypeError):
            self.op.addition(5)


class TestSubtraction(unittest.TestCase):
    def setUp(self):
        self.op = Operators()

    def test_multiple_subtraction(self):
        self.assertEqual(self.op.subtraction("44 - 1 - 300 - 13.7 - 99.9 - 5.82"), -376.42)

    def test_random_subtraction(self):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        self.assertEqual(self.op.subtraction(f'{n1} - {n2}'), n1 - n2)

    def test_invalid_subtraction(self):
        with self.assertRaises(TypeError):
            self.op.subtraction(5)


class TestMultiplication(unittest.TestCase):
    def setUp(self):
        self.op = Operators()

    def test_multiple_multiplication(self):
        self.assertEqual(self.op.multiplication("10000 * 1000 * 100 * 10 * 1 * 0.1"), 1000000000)

    def test_random_multiplication(self):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        self.assertEqual(self.op.multiplication(f'{n1} * {n2}'), n1 * n2)

    def test_invalid_multiplication(self):
        with self.assertRaises(TypeError):
            self.op.multiplication(5)


class TestDivision(unittest.TestCase):
    def setUp(self):
        self.op = Operators()

    def test_multiple_division(self):
        self.assertEqual(self.op.division("10000 / 1000 / 100 / 10 / 1"), 0.01)

    def test_random_division(self):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        self.assertEqual(self.op.division(f'{n1} / {n2}'), n1 / n2)

    def test_invalid_division(self):
        with self.assertRaises(TypeError):
            self.op.division(5)

    def test_divide_by_zero(self):
        n = random.randint(1, 1000000)
        self.assertEqual(self.op.division(f'{n} / 0'), None)


if __name__ == "__main__":
    unittest.main()
