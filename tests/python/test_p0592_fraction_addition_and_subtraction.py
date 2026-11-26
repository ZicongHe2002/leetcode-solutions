from fractions import Fraction
from itertools import product
from math import gcd
import random
import re
import unittest

from python.p0592_fraction_addition_and_subtraction import Solution


def fraction_oracle(expression):
    terms = re.findall(r'[+-]?\d+/\d+', expression)
    self_sum = sum((Fraction(term) for term in terms), Fraction(0))
    return f'{self_sum.numerator}/{self_sum.denominator}'


def expression_from_terms(terms):
    expression = ''.join(('+' if sign > 0 else '-') + f'{top}/{bottom}'
                         for sign, top, bottom in terms)
    return expression[1:] if expression.startswith('+') else expression


class FractionSumTests(unittest.TestCase):
    def check(self, expression, expected=None):
        result = Solution().fractionAddition(expression)
        self.assertIs(type(result), str)
        self.assertEqual(result, fraction_oracle(expression) if expected is None else expected)
        top, bottom = map(int, result.split('/'))
        self.assertGreater(bottom, 0)
        self.assertEqual(gcd(abs(top), bottom), 1)
        self.assertEqual(result, f'{top}/{bottom}')

    def test_all_small_signed_term_sequences_and_ten_term_seeded_cases(self):
        terms = [(sign, top, bottom) for sign in (-1, 1)
                 for top in range(1, 4) for bottom in range(1, 4) if gcd(top, bottom) == 1]
        self.assertEqual(len(terms), 14)
        cases = 0
        for size in range(1, 5):
            for sequence in product(terms, repeat=size):
                self.check(expression_from_terms(sequence))
                cases += 1
        self.assertEqual(cases, 41370)
        legal = [(sign, top, bottom) for sign in (-1, 1)
                 for top in range(1, 11) for bottom in range(1, 11) if gcd(top, bottom) == 1]
        rng = random.Random(592)
        for _ in range(300):
            self.check(expression_from_terms([rng.choice(legal) for _ in range(10)]))

    def test_multi_digit_cancellation_integers_and_samples(self):
        for expression, expected in (
            ('-1/2+1/2', '0/1'), ('-1/2+1/2+1/3', '1/3'), ('1/3-1/2', '-1/6'),
            ('10/1-10/1', '0/1'), ('1/10+1/5+3/10+2/5', '1/1'),
            ('-10/3-2/3', '-4/1'), ('10/1', '10/1'), ('-1/10', '-1/10'),
        ):
            self.check(expression, expected)
        self.check('+'.join(['10/1'] * 10), '100/1')
        self.check('-10/1' * 10, '-100/1')


if __name__ == '__main__':
    unittest.main()
