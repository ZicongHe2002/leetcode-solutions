from itertools import product
import unittest

from python.p0532_k_diff_pairs_in_an_array import Solution


def distinct_index_pairs_oracle(values, difference):
    pairs = set()
    for left in range(len(values)):
        for right in range(left + 1, len(values)):
            if abs(values[left] - values[right]) == difference:
                pairs.add(tuple(sorted((values[left], values[right]))))
    return len(pairs)


class DistinctValueDifferenceTests(unittest.TestCase):
    def check(self, values, difference, expected=None):
        before = values[:]
        actual = Solution().findPairs(values, difference)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, distinct_index_pairs_oracle(values, difference) if expected is None else expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_and_differences_against_index_pairs(self):
        arrays = queries = 0
        for size in range(1, 8):
            for values in product((-1, 0, 1), repeat=size):
                arrays += 1
                for difference in range(5):
                    self.check(list(values), difference)
                    queries += 1
        self.assertEqual((arrays, queries), (3279, 16395))

    def test_maximum_count_zero_difference_and_numeric_limits(self):
        self.check([0] * 10000, 0, 1)
        self.check([0] * 10000, 1, 0)
        self.check(list(range(10000)), 1, 9999)
        self.check(list(range(10000)), 0, 0)
        values = [-10**7, 0, 10**7] * 3333 + [-10**7]
        self.assertEqual(len(values), 10000)
        self.check(values, 10**7, 2)
        self.check(values, 0, 3)
        self.check([3, 1, 4, 1, 5], 2, 2)
        self.check([1], 0, 0)


if __name__ == '__main__':
    unittest.main()
