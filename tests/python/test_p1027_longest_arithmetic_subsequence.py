from itertools import product
import unittest

from python.p1027_longest_arithmetic_subsequence import Solution


def longest_retained_arithmetic_subset(values):
    longest = 2
    for mask in range(1 << len(values)):
        if mask.bit_count() < 2:
            continue
        selected = [value for index, value in enumerate(values) if mask >> index & 1]
        difference = selected[1] - selected[0]
        if all(selected[index] - selected[index - 1] == difference
               for index in range(2, len(selected))):
            longest = max(longest, len(selected))
    return longest


class ArithmeticSubsequenceLengthTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = longest_retained_arithmetic_subset(values)
        result = Solution().longestArithSeqLength(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_every_retained_index_subset(self):
        checks = 0
        for size in range(2, 9):
            for values in product((0, 1, 2), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 9837)

    def test_current_maximum_length_zero_negative_and_extreme_differences(self):
        self.check([7] * 1500, 1500)
        self.check([0, 500] * 750, 750)
        self.check([value for value in range(500) for _ in range(3)], 500)
        self.check(list(range(501)), 501)
        self.check(list(range(500, -1, -1)), 501)
        self.check([9, 4, 7, 2, 10], 3)
        self.check([20, 1, 15, 3, 10, 5, 8], 4)


if __name__ == '__main__':
    unittest.main()
