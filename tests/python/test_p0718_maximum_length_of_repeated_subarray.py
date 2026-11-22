import unittest
from itertools import product

from python.p0718_maximum_length_of_repeated_subarray import Solution


def contiguous_slice_set(values):
    return {tuple(values[start:end]) for start in range(len(values))
            for end in range(start + 1, len(values) + 1)}


def common_slice_length(first, second):
    return max(map(len, contiguous_slice_set(first) & contiguous_slice_set(second)), default=0)


class RepeatedSubarrayTests(unittest.TestCase):
    def check(self, first, second, expected=None):
        before_first, before_second = first[:], second[:]
        if expected is None:
            expected = common_slice_length(first, second)
        result = Solution().findLength(first, second)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(first, before_first)
        self.assertEqual(second, before_second)

    def test_all_small_binary_array_pairs_against_slice_intersection(self):
        arrays = [list(values) for size in range(6) for values in product((0, 1), repeat=size)]
        checks = 0
        for first in arrays:
            for second in arrays:
                self.check(first, second)
                checks += 1
        self.assertEqual(checks, 3969)

    def test_maximum_lengths_shift_and_contiguity_breaks(self):
        self.check([0] * 1000, [0] * 1000, 1000)
        self.check([0, 1] * 500, [1, 0] * 500, 999)
        self.check([0] * 1000, [100] * 1000, 0)
        self.check([0] * 499 + [100] + [0] * 500, [0] * 1000, 500)
        self.check([1, 2, 3], [1, 9, 2, 9, 3], 1)


if __name__ == '__main__':
    unittest.main()
