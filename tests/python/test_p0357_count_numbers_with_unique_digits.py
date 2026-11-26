from functools import lru_cache
import unittest

from python.p0357_count_numbers_with_unique_digits import Solution


@lru_cache(None)
def digit_mask_oracle(remaining, used, started):
    if remaining == 0:
        return 1
    count = 0
    for digit in range(10):
        if not started and digit == 0:
            count += digit_mask_oracle(remaining - 1, 0, False)
        elif not used & (1 << digit):
            count += digit_mask_oracle(remaining - 1, used | (1 << digit), True)
    return count


class UniqueDigitLengthCountTests(unittest.TestCase):
    def test_entire_original_domain_against_digit_state_enumeration(self):
        for n in range(9):
            actual = Solution().countNumbersWithUniqueDigits(n)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, digit_mask_oracle(n, 0, False))
        self.assertEqual(Solution().countNumbersWithUniqueDigits(0), 1)
        self.assertEqual(Solution().countNumbersWithUniqueDigits(1), 10)
        self.assertEqual(Solution().countNumbersWithUniqueDigits(2), 91)
        self.assertEqual(Solution().countNumbersWithUniqueDigits(8), 2345851)

    def test_small_powers_against_direct_integer_representation(self):
        for n in range(6):
            expected = sum(len(set(str(value))) == len(str(value)) for value in range(10**n))
            self.assertEqual(digit_mask_oracle(n, 0, False), expected)
            self.assertEqual(Solution().countNumbersWithUniqueDigits(n), expected)


if __name__ == '__main__':
    unittest.main()
