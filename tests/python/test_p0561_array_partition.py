from functools import lru_cache
from itertools import product
import unittest

from python.p0561_array_partition import Solution


@lru_cache(None)
def every_perfect_matching_oracle(values):
    if not values:
        return 0
    return max(min(values[0], values[partner]) +
               every_perfect_matching_oracle(values[1:partner] + values[partner + 1:])
               for partner in range(1, len(values)))


class AdjacentMinimumPairTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        actual = Solution().arrayPairSum(values)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, every_perfect_matching_oracle(tuple(values)) if expected is None else expected)
        self.assertEqual(values, before)

    def test_all_small_even_arrays_against_every_perfect_matching(self):
        arrays = 0
        for size in (2, 4, 6, 8):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                arrays += 1
        self.assertEqual(arrays, 7380)

    def test_maximum_size_negative_totals_duplicates_and_value_limits(self):
        self.check([-10000] * 20000, -100000000)
        self.check([10000] * 20000, 100000000)
        self.check([-10000, 10000] * 10000, 0)
        self.check(list(range(-10000, 10000)), -10000)
        self.check([-10000, 10000], -10000)
        self.check([1, 4, 3, 2], 4)
        self.check([6, 2, 6, 5, 1, 2], 9)


if __name__ == '__main__':
    unittest.main()
