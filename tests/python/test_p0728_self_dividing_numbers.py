import unittest
from math import lcm

from python.p0728_self_dividing_numbers import Solution


def digit_lcm_accepts(value):
    digits = str(value)
    return '0' not in digits and value % lcm(*(int(char) for char in digits)) == 0


class SelfDividingNumbersTests(unittest.TestCase):
    def check(self, left, right, expected=None):
        result = Solution().selfDividingNumbers(left, right)
        self.assertIs(type(result), list)
        self.assertEqual(result, [value for value in range(left, right + 1) if digit_lcm_accepts(value)]
                         if expected is None else expected, (left, right))
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result, sorted(set(result)))

    def test_every_contract_integer_and_all_small_closed_intervals_against_digit_lcm(self):
        for value in range(1, 10001):
            self.check(value, value)
        checked = 0
        for left in range(1, 101):
            for right in range(left, 101):
                self.check(left, right)
                checked += 1
        self.assertEqual(checked, 5050)

    def test_examples_zero_digits_and_full_range(self):
        self.check(1, 22, [1,2,3,4,5,6,7,8,9,11,12,15,22])
        self.check(47, 85, [48,55,66,77])
        self.check(10000, 10000, [])
        self.check(101, 101, [])
        self.check(128, 128, [128])
        self.check(1, 10000)


if __name__ == '__main__':
    unittest.main()
