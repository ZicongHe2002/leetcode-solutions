from itertools import combinations, product
import unittest

from python.p0334_increasing_triplet_subsequence import Solution


def every_index_triple(values):
    return any(values[left] < values[middle] < values[right]
               for left, middle, right in combinations(range(len(values)), 3))


class StrictIncreasingTripleTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = every_index_triple(values)
        result = Solution().increasingTriplet(values)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_every_index_triple(self):
        checks = 0
        for size in range(1, 9):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_duplicate_thresholds_and_signed_endpoints(self):
        self.check([7] * 500000, False)
        self.check(list(range(500000, 0, -1)), False)
        self.check([0, 1] * 250000, False)
        self.check([0] * 499998 + [1, 2], True)
        self.check([2, 3, 1, 4], True)
        self.check([2, 3, 1, 2], False)
        self.check([-2**31, -2**31 + 1, 2**31 - 1], True)
        self.check([2**31 - 1] * 3, False)


if __name__ == '__main__':
    unittest.main()
