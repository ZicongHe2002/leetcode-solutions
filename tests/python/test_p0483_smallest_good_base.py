import unittest

from python.p0483_smallest_good_base import Solution


def all_digits_one(number, base):
    digits = 0
    while number:
        number, digit = divmod(number, base)
        if digit != 1:
            return False
        digits += 1
    return digits >= 2


def increasing_base_oracle(number):
    for base in range(2, number):
        if all_digits_one(number, base):
            return base
    raise AssertionError('base n-1 must work')


class ExactGoodBaseTests(unittest.TestCase):
    def check(self, number, expected=None):
        result = Solution().smallestGoodBase(str(number))
        self.assertIs(type(result), str)
        base = int(result)
        self.assertEqual(result, str(base))
        self.assertGreaterEqual(base, 2)
        self.assertTrue(all_digits_one(number, base))
        self.assertEqual(base, increasing_base_oracle(number) if expected is None else expected)

    def test_all_small_numbers_against_increasing_bases_and_division(self):
        checks = 0
        for number in range(3, 3001):
            self.check(number)
            checks += 1
        self.assertEqual(checks, 2998)

    def test_large_exact_repunits_decimal_limit_and_original_examples(self):
        self.check((1 << 59) - 1, 2)
        ternary = (3**38 - 1) // 2
        self.assertEqual(ternary % 2, 0)
        self.assertLessEqual(ternary, 10**18)
        self.check(ternary, 3)
        self.check(10**18, 10**18 - 1)
        self.check(13, 3)
        self.check(4681, 8)
        self.check(3, 2)


if __name__ == '__main__':
    unittest.main()
