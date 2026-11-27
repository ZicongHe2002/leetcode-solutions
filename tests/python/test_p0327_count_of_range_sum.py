from itertools import product
import unittest

from python.p0327_count_of_range_sum import Solution


def direct_nonempty_subarray_sums(values, lower, upper):
    count = 0
    for left in range(len(values)):
        total = 0
        for right in range(left, len(values)):
            total += values[right]
            count += lower <= total <= upper
    return count


class InclusiveRangeSumCountTests(unittest.TestCase):
    def check(self, values, lower, upper, expected=None):
        before = values[:]
        if expected is None:
            expected = direct_nonempty_subarray_sums(values, lower, upper)
        self.assertLessEqual(expected, 2**31 - 1)
        result = Solution().countRangeSum(values, lower, upper)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_and_inclusive_lower_upper_bounds(self):
        bounds = [(lower, upper) for lower in range(-2, 3) for upper in range(lower, 3)]
        arrays = queries = 0
        for size in range(1, 8):
            for values in product((-1, 0, 1), repeat=size):
                for lower, upper in bounds:
                    self.check(list(values), lower, upper)
                    queries += 1
                arrays += 1
        self.assertEqual((arrays, queries), (3279, 49185))

    def test_maximum_length_legal_large_answer_and_wide_prefix_values(self):
        self.check([1] * 100000, 1, 1, 100000)
        self.check([1] * 100000, 100000, 100000, 1)
        size = 65535
        self.check([0] * size, 0, 0, size * (size + 1) // 2)
        value = 2**31 - 1
        self.check([value] * 50000 + [-value] * 50000, 0, 0, 50000)
        self.check([-2**31, 2**31 - 1], -1, -1, 1)
        self.check([-2, 5, -1], -2, 2, 3)


if __name__ == '__main__':
    unittest.main()
