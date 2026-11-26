import ast
from fractions import Fraction
from functools import lru_cache
from itertools import product
import unittest

from python.p0553_optimal_division import Solution


def every_parenthesization_oracle(values):
    @lru_cache(None)
    def possibilities(start, end):
        if end - start == 1:
            return frozenset((Fraction(values[start]),))
        return frozenset(left / right for middle in range(start + 1, end)
                         for left in possibilities(start, middle)
                         for right in possibilities(middle, end))

    return max(possibilities(0, len(values)))


def parse_exact_division(text):
    leaves = []

    def value(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            leaves.append(node.value)
            return Fraction(node.value)
        if not isinstance(node, ast.BinOp) or not isinstance(node.op, ast.Div):
            raise AssertionError('Expected only ordered integer leaves and division')
        return value(node.left) / value(node.right)

    result = value(ast.parse(text, mode='eval').body)
    return result, leaves


class ExactMaximumDivisionTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        expression = Solution().optimalDivision(values)
        self.assertIs(type(expression), str)
        actual, leaves = parse_exact_division(expression)
        self.assertEqual(leaves, values)
        self.assertEqual(actual, every_parenthesization_oracle(tuple(values)))
        self.assertEqual(expression.count('('), int(len(values) >= 3))
        self.assertEqual(expression.count(')'), int(len(values) >= 3))
        self.assertEqual(values, before)

    def test_all_short_arrays_against_exact_all_parenthesizations(self):
        arrays = 0
        for size in range(1, 7):
            for values in product((2, 3, 4), repeat=size):
                self.check(list(values))
                arrays += 1
        self.assertEqual(arrays, 1092)

    def test_maximum_length_values_nonintegral_results_and_no_redundant_parentheses(self):
        self.check([1000] * 10)
        self.check(list(range(1000, 990, -1)))
        self.check([2] * 10)
        self.check([1000, 100, 10, 2])
        self.check([2, 3, 4])
        self.check([1000])
        self.check([2, 1000])
        self.assertEqual(Solution().optimalDivision([1000, 100, 10, 2]), '1000/(100/10/2)')


if __name__ == '__main__':
    unittest.main()
