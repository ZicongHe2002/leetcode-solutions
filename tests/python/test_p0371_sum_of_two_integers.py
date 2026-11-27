import ast
import inspect
import unittest

import python.p0371_sum_of_two_integers as implementation


class MaskedAdditionTests(unittest.TestCase):
    def check(self, first, second):
        self.assertTrue(-1000 <= first <= 1000)
        self.assertTrue(-1000 <= second <= 1000)
        result = implementation.Solution().getSum(first, second)
        self.assertIs(type(result), int)
        self.assertEqual(result, first + second)

    def test_all_small_signed_pairs_against_normal_addition(self):
        checks = 0
        for first in range(-32, 33):
            for second in range(-32, 33):
                self.check(first, second)
                checks += 1
        self.assertEqual(checks, 4225)

    def test_original_bounds_carry_chains_and_forbidden_operators(self):
        values = (-1000, -999, -513, -512, -1, 0, 1, 511, 512, 999, 1000)
        for first in values:
            for second in values:
                self.check(first, second)
        for bit in range(10):
            self.check(2**bit - 1, 1)
            self.check(-(2**bit), -1)
            self.check(-1, 2**bit)
        tree = ast.parse(inspect.getsource(implementation.Solution))
        self.assertFalse(any(isinstance(node, (ast.Add, ast.Sub)) for node in ast.walk(tree)))


if __name__ == '__main__':
    unittest.main()
