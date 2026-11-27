import ast
from fractions import Fraction
from itertools import product
import re
import unittest

from python.p0227_basic_calculator_ii import Solution


def ast_fraction_oracle(text):
    normalized = re.sub(r'[0-9]+', lambda match: str(int(match.group())), text.strip())

    def visit(node):
        if isinstance(node, ast.Constant):
            return node.value
        left, right = visit(node.left), visit(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        return int(Fraction(left, right))

    return visit(ast.parse(normalized, mode='eval').body)


class CalculatorPrecedenceTests(unittest.TestCase):
    def test_all_small_valid_expressions_against_ast_and_exact_rationals(self):
        cases = 0
        for size in range(1, 5):
            for numbers in product(range(4), repeat=size):
                for signs in product('+-*/', repeat=size - 1):
                    if any(sign == '/' and numbers[index + 1] == 0 for index, sign in enumerate(signs)):
                        continue
                    text = '  ' + str(numbers[0]) + ''.join('  ' + sign + '  ' + str(numbers[index + 1]) for index, sign in enumerate(signs)) + '  '
                    actual = Solution().calculate(text)
                    self.assertIs(type(actual), int)
                    self.assertEqual(actual, ast_fraction_oracle(text))
                    cases += 1
        self.assertEqual(cases, 14464)

    def test_truncation_leading_zeroes_int32_values_and_long_chain(self):
        for text, expected in [('3+2*2', 7), (' 3/2 ', 1), ('0-3/2', -1), ('1-7/3*2', -3), ('0012 + 0003*04', 24), ('2147483647+0', 2147483647), ('0-2147483647/2', -1073741823)]:
            self.assertEqual(Solution().calculate(text), expected)
        text = '1+' * 99999 + '1'
        self.assertEqual(len(text), 199999)
        self.assertEqual(Solution().calculate(text), 100000)


if __name__ == '__main__':
    unittest.main()
