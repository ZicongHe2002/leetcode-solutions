from itertools import product
import unittest

from python.p0414_third_maximum_number import Solution


def distinct_rank_oracle(values):
    unique = set(values)
    if len(unique) < 3:
        return max(unique)
    return next(value for value in unique if sum(other > value for other in unique) == 2)


class ThirdDistinctMaximumTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        actual = Solution().thirdMax(values)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, distinct_rank_oracle(values) if expected is None else expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_complete_distinct_rank_definition(self):
        arrays = 0
        for size in range(1, 8):
            for values in product((-2, -1, 0, 1, 2), repeat=size):
                self.check(list(values))
                arrays += 1
        self.assertEqual(arrays, 97655)

    def test_duplicates_fallbacks_int32_minimum_and_maximum_length(self):
        self.check([2, 2, 3, 1], 1)
        self.check([1, 2], 2)
        self.check([1, 1, 2], 2)
        self.check([2**31 - 1, 0, -2**31], -2**31)
        self.check([-2**31] * 10000, -2**31)
        self.check(list(range(1, 10001)), 9998)


if __name__ == '__main__':
    unittest.main()
