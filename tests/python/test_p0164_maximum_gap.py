from itertools import product
import unittest

from python.p0164_maximum_gap import Solution


class LinearBucketGapTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        ordered = sorted(values)
        expected = max((right - left for left, right in zip(ordered, ordered[1:])), default=0)
        result = Solution().maximumGap(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_nonnegative_arrays_against_sorted_gaps(self):
        checks = 0
        for size in range(1, 7):
            for values in product((0, 1, 3, 7), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 5460)

    def test_maximum_length_span_equal_values_and_bucket_boundaries(self):
        self.check([0] * 99999 + [10**9])
        self.check([10**9] * 100000)
        self.check([index * 10000 for index in range(100000)])
        self.check(list(range(99999, -1, -1)))
        self.check([0, 1, 10**9 - 1, 10**9])


if __name__ == '__main__':
    unittest.main()
