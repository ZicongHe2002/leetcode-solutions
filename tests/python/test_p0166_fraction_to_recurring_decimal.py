from fractions import Fraction
import re
import unittest

from python.p0166_fraction_to_recurring_decimal import Solution


def decimal_integer(digits):
    result = 0
    for start in range(0, len(digits), 200):
        block = digits[start:start + 200]
        result = result * 10**len(block) + int(block)
    return result


def decimal_prefix_and_period(denominator):
    twos = fives = 0
    while denominator % 2 == 0:
        twos += 1
        denominator //= 2
    while denominator % 5 == 0:
        fives += 1
        denominator //= 5
    if denominator == 1:
        return max(twos, fives), 0
    residue, period = 10 % denominator, 1
    while residue != 1:
        residue = residue * 10 % denominator
        period += 1
    return max(twos, fives), period


class FractionExactValueAndPeriodTests(unittest.TestCase):
    def check(self, numerator, denominator):
        expected = Fraction(numerator, denominator)
        result = Solution().fractionToDecimal(numerator, denominator)
        self.assertIs(type(result), str)
        self.assertLess(len(result), 10000)
        if expected.denominator == 1:
            self.assertEqual(result, str(expected.numerator))
            return result
        match = re.fullmatch(r'(-?)(0|[1-9][0-9]*)\.([0-9]*)(?:\(([0-9]+)\))?', result)
        self.assertIsNotNone(match)
        sign, whole, prefix, cycle = match.groups()
        cycle = cycle or ''
        wanted_prefix, wanted_period = decimal_prefix_and_period(expected.denominator)
        self.assertEqual((len(prefix), len(cycle)), (wanted_prefix, wanted_period))
        actual = Fraction(int(whole)) + Fraction(decimal_integer(prefix), 10**len(prefix))
        if cycle:
            actual += Fraction(decimal_integer(cycle), 10**len(prefix) * (10**len(cycle) - 1))
        if sign:
            actual = -actual
        self.assertEqual(actual, expected)
        return result

    def test_all_small_signed_fractions_exact_value_and_chosen_minimal_cycle(self):
        checked = 0
        for numerator in range(-20, 21):
            for denominator in range(-20, 21):
                if denominator:
                    self.check(numerator, denominator)
                    checked += 1
        self.assertEqual(checked, 1640)

    def test_int32_limits_finite_required_and_near_maximum_answer_length(self):
        for numerator, denominator in ((-2**31, -1), (-2**31, 1), (1, -2**31),
                                       (2**31 - 1, -2**31), (-2**31, -2**31),
                                       (0, -1), (4, 333), (1, 6), (1, 8)):
            self.check(numerator, denominator)
        result = self.check(1, 9967)
        self.assertEqual(len(result), 9970)
        self.assertEqual(self.check(1, 2), '0.5')
        self.assertEqual(self.check(4, 333), '0.(012)')


if __name__ == '__main__':
    unittest.main()
