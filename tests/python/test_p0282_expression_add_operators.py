import ast
from collections import defaultdict
from itertools import product
import re
import unittest

from python.p0282_expression_add_operators import Solution


def ast_value(expression):
    def visit(node):
        if isinstance(node, ast.Constant):
            return node.value
        left, right = visit(node.left), visit(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        return left * right
    return visit(ast.parse(expression, mode='eval').body)


def all_gap_insertions_oracle(digits):
    values = defaultdict(set)
    for gaps in product(('', '+', '-', '*'), repeat=len(digits) - 1):
        text = ''.join(digit + (gaps[index] if index < len(gaps) else '') for index, digit in enumerate(digits))
        if any(len(token) > 1 and token.startswith('0') for token in re.findall('[0-9]+', text)):
            continue
        values[ast_value(text)].add(text)
    return values


class OperatorInsertionTests(unittest.TestCase):
    def check(self, digits, target, expected):
        result = Solution().addOperators(digits, target)
        self.assertIs(type(result), list)
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(set(result), expected)

    def test_all_small_digit_strings_and_targets_against_gap_enumeration_ast(self):
        queries = 0
        strings = 0
        for size in range(1, 6):
            for characters in product('012', repeat=size):
                digits = ''.join(characters)
                expected = all_gap_insertions_oracle(digits)
                for target in range(-6, 7):
                    self.check(digits, target, expected[target])
                    queries += 1
                strings += 1
        self.assertEqual((strings, queries), (363, 4719))

    def test_leading_zeroes_multiplicative_sign_and_maximum_digit_length(self):
        self.check('105', 5, {'1*0+5', '10-5'})
        self.check('232', 8, {'2+3*2', '2*3+2'})
        self.check('123', -5, {'1-2*3'})
        self.check('00', 0, {'0+0', '0-0', '0*0'})
        digits = '0' * 10
        expected = {'0' + ''.join(sign + '0' for sign in signs) for signs in product('+-*', repeat=9)}
        self.assertEqual(len(expected), 19683)
        self.check(digits, 0, expected)
        large = '2147483647'
        result = Solution().addOperators(large, 2147483647)
        self.assertIn(large, result)
        self.assertEqual(len(result), len(set(result)))
        for expression in result:
            self.assertEqual(ast_value(expression), 2147483647)


if __name__ == '__main__':
    unittest.main()
