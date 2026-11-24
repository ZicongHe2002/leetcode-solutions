import unittest
from itertools import product

from python.p0209_minimum_size_subarray_sum import Solution


def all_intervals(values, target):
    lengths = [end - start for start in range(len(values))
               for end in range(start + 1, len(values) + 1)
               if sum(values[start:end]) >= target]
    return min(lengths, default=0)


class MinimumSumWindowTests(unittest.TestCase):
    def check(self, values, target, expected=None):
        before = values[:]
        if expected is None:
            expected = all_intervals(values, target)
        result = Solution().minSubArrayLen(target, values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_positive_small_arrays_against_all_intervals(self):
        arrays = checks = 0
        for size in range(7):
            for values in product((1, 2, 3), repeat=size):
                arrays += 1
                for target in range(1, sum(values) + 2):
                    self.check(list(values), target)
                    checks += 1
        self.assertEqual((arrays, checks), (1093, 13123))

    def test_maximum_lengths_and_target_boundaries(self):
        self.check([1] * 100000, 100000, 100000)
        self.check([1] * 100000, 10**9, 0)
        self.check([10000] * 100000, 10**9, 100000)
        self.check([10000] * 100000, 10000, 1)
        self.check([2, 3, 1, 2, 4, 3], 7, 2)
        self.check([1], 2, 0)


if __name__ == '__main__':
    unittest.main()
