import random
import unittest
from fractions import Fraction
from itertools import product

from python.p0772_basic_calculator_iii import Solution


def evaluate_ast(node):
    if type(node) is int:
        return node
    operator, left, right = node
    a, b = evaluate_ast(left), evaluate_ast(right)
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    return int(Fraction(a, b))


def render_ast(node):
    if type(node) is int:
        return str(node)
    operator, left, right = node
    return '(' + render_ast(left) + ' ' + operator + ' ' + render_ast(right) + ')'


class CalculatorThreeTests(unittest.TestCase):
    def check(self, expression, expected):
        result = Solution().calculate(expression)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, expression[:200])

    def test_all_small_two_operator_expressions_and_seeded_nested_asts_against_exact_fraction_truncation(self):
        precedence = {'+':1, '-':1, '*':2, '/':2}
        checked = 0
        for a,b,c in product(range(4), repeat=3):
            for first, second in product('+-*/', repeat=2):
                node = (second, (first,a,b), c) if precedence[first] >= precedence[second] else (first,a,(second,b,c))
                try:
                    expected = evaluate_ast(node)
                except ZeroDivisionError:
                    continue
                self.check(f'{a} {first} {b} {second} {c}', expected)
                checked += 1
        self.assertGreater(checked, 800)
        rng = random.Random(772)

        def tree(depth):
            if not depth or rng.randrange(4) == 0:
                return rng.randrange(10)
            return (rng.choice('+-*/'), tree(depth - 1), tree(depth - 1))

        accepted = 0
        for _ in range(10000):
            node = tree(3)
            try:
                expected = evaluate_ast(node)
            except ZeroDivisionError:
                continue
            self.check(render_ast(node), expected)
            accepted += 1
            if accepted == 200:
                break
        self.assertEqual(accepted, 200)

    def test_official_examples_signed_division_long_inputs_and_separate_unary_extensions(self):
        self.check('1 + 1', 2)
        self.check('6-4/2', 4)
        self.check('2*(5+5*2)/3+(6/2+8)', 21)
        self.check('(2+6*3+5-(3*14/7+2)*5)+3', -12)
        self.check('(1-8)/3', -2)
        self.check('7/(1-4)', -2)
        self.check('(0-2147483647-1)/3', -715827882)
        self.check('2147483647', 2147483647)
        self.check('(' * 4999 + '1' + ')' * 4999, 1)
        self.check('1+' * 4999 + '1', 5000)
        # Extensions beyond the nonnegative-literal binary-expression contract.
        self.check('-(2+3)*-2', 10)
        self.check('--2 + +3', 5)
        self.check('-7 / 3', -2)


if __name__ == '__main__':
    unittest.main()
