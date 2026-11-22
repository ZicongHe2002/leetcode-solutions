from itertools import product
import unittest

from python.p0446_arithmetic_slices_ii_subsequence import Solution


def retained_index_subset_count(values):
    total = 0
    for mask in range(1 << len(values)):
        if mask.bit_count() < 3:
            continue
        selected = [value for index, value in enumerate(values) if mask >> index & 1]
        difference = selected[1] - selected[0]
        total += all(selected[index] - selected[index - 1] == difference
                     for index in range(2, len(selected)))
    return total


def complete_progression_subsequence_count(length):
    return sum((length - 1 - start) // step - 1
               for step in range(1, (length - 1) // 2 + 1)
               for start in range(length - 2 * step))


class ArithmeticIndexSubsequenceCountTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = retained_index_subset_count(values)
        self.assertLessEqual(expected, 2**31 - 1)
        result = Solution().numberOfArithmeticSlices(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_every_retained_index_subset(self):
        checks = 0
        for size in range(1, 8):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_length_legal_large_count_and_wide_signed_differences(self):
        expected = complete_progression_subsequence_count(1000)
        self.check(list(range(-500, 500)), expected)
        self.check(list(range(499, -501, -1)), expected)
        self.check([7] * 31, 2**31 - 1 - 31 - 31 * 30 // 2)
        self.check([-2**31, -1, 2**31 - 2], 1)
        self.check([2**31 - 1, 0, -2**31 + 1], 1)
        self.check([-2**31, 2**31 - 1, -2**31, 2**31 - 1], 0)


if __name__ == '__main__':
    unittest.main()
