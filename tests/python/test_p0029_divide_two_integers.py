import ast
import inspect
import unittest

import python.p0029_divide_two_integers as implementation


def reference(dividend, divisor):
    magnitude = abs(dividend) // abs(divisor)
    result = -magnitude if (dividend < 0) != (divisor < 0) else magnitude
    return min(2147483647, max(-2147483648, result))


class SignedDivisionTests(unittest.TestCase):
    def check(self, dividend, divisor):
        result = implementation.Solution().divide(dividend, divisor)
        self.assertIs(type(result), int)
        self.assertEqual(result, reference(dividend, divisor))
        self.assertTrue(-2147483648 <= result <= 2147483647)

    def test_all_small_signed_inputs_against_absolute_integer_division(self):
        checks = 0
        for dividend in range(-128, 129):
            for divisor in range(-32, 33):
                if divisor:
                    self.check(dividend, divisor)
                    checks += 1
        self.assertEqual(checks, 16448)

    def test_32bit_boundaries_and_forbidden_operator_contract(self):
        values = [-2147483648, -2147483647, -1073741825, -1073741824,
                  -65537, -1, 0, 1, 65537, 1073741823, 2147483646, 2147483647]
        for dividend in values:
            for divisor in values:
                if divisor:
                    self.check(dividend, divisor)
        for bit in range(31):
            for offset in (-1, 0, 1):
                value = (1 << bit) + offset
                for dividend in (value, -value):
                    for divisor in (1, -1, 2, -2, 3, -3):
                        self.check(dividend, divisor)
        tree = ast.parse(inspect.getsource(implementation.Solution))
        self.assertFalse(any(isinstance(node, (ast.Mult, ast.Div, ast.FloorDiv, ast.Mod))
                             for node in ast.walk(tree)))


if __name__ == '__main__':
    unittest.main()
