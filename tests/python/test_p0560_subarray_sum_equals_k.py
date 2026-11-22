import unittest
from itertools import product

from python.p0560_subarray_sum_equals_k import Solution


def all_interval_sums(values, target):
    return sum(sum(values[start:end]) == target for start in range(len(values))
               for end in range(start + 1, len(values) + 1))


class PrefixSumCountTests(unittest.TestCase):
    def check(self, values, target, expected=None):
        before = values[:]
        if expected is None:
            expected = all_interval_sums(values, target)
        result = Solution().subarraySum(values, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_and_targets_against_slices(self):
        arrays = checks = 0
        for size in range(8):
            for values in product((-1, 0, 1), repeat=size):
                arrays += 1
                for target in range(-size - 1, size + 2):
                    self.check(list(values), target)
                    checks += 1
        self.assertEqual((arrays, checks), (3280, 52488))

    def test_maximum_lengths_signed_limits_and_repeated_prefixes(self):
        self.check([0] * 20000, 0, 200010000)
        self.check([1000] * 20000, 10**7, 10001)
        self.check([-1000] * 20000, -(10**7), 10001)
        self.check([1, -1] * 10000, 0, 100000000)
        self.check([0], 0, 1)


if __name__ == '__main__':
    unittest.main()
