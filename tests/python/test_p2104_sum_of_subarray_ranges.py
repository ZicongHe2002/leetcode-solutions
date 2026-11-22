import unittest
from itertools import product

from python.p2104_sum_of_subarray_ranges import Solution


def all_slice_ranges(values):
    return sum(max(values[left:right]) - min(values[left:right]) for left in range(len(values))
               for right in range(left + 1, len(values) + 1))


class SubarrayRangeTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = all_slice_ranges(values)
        result = Solution().subArrayRanges(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertGreaterEqual(result, 0)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_against_direct_extrema(self):
        checks = 0
        for size in range(7):
            for values in product(range(-2, 3), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 19531)

    def test_maximum_length_signed_limits_ties_and_large_exact_sum(self):
        count = 1000
        self.check([10**9] * count, 0)
        self.check([-10**9, 10**9] * 500, 2 * 10**9 * count * (count - 1) // 2)
        expected = count * (count - 1) * (count + 1) // 6
        self.check(list(range(count)), expected)
        self.check(list(range(count - 1, -1, -1)), expected)
        self.check([1, 3, 3], 4)
        self.check([-1, -1, 1], 4)


if __name__ == '__main__':
    unittest.main()
