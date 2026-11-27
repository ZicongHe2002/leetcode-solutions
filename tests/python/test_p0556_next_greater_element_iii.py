from itertools import permutations, product
import unittest

from python.p0556_next_greater_element_iii import Solution


def all_digit_permutations_oracle(number):
    candidates = (int(''.join(order)) for order in set(permutations(str(number))) if order[0] != '0')
    return min((value for value in candidates if number < value <= 2**31 - 1), default=-1)


class BoundedNextDigitPermutationTests(unittest.TestCase):
    def check(self, number, expected=None):
        actual = Solution().nextGreaterElement(number)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, all_digit_permutations_oracle(number) if expected is None else expected)

    def test_all_short_positive_numbers_over_small_digits_against_every_permutation(self):
        numbers = 0
        for size in range(1, 7):
            for first in '123':
                for tail in product('0123', repeat=size - 1):
                    self.check(int(first + ''.join(tail)))
                    numbers += 1
        self.assertEqual(numbers, 4095)

    def test_exact_32bit_limit_overflow_descending_and_zero_digits(self):
        self.check(2147483476, 2147483647)
        self.check(2147483486, -1)
        self.check(2147483647, -1)
        self.check(1999999999, -1)
        self.check(999999999, -1)
        self.check(1200, 2001)
        self.check(102, 120)
        self.check(10, -1)
        self.check(12, 21)
        self.check(21, -1)
        self.check(1, -1)


if __name__ == '__main__':
    unittest.main()
