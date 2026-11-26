from itertools import product
import unittest

from python.p0220_contains_duplicate_iii import Solution


def all_pairs_oracle(values, index_diff, value_diff):
    return any(right - left <= index_diff and abs(values[right] - values[left]) <= value_diff
               for left in range(len(values)) for right in range(left + 1, len(values)))


class NearbyAlmostDuplicateTests(unittest.TestCase):
    def check(self, values, index_diff, value_diff, expected=None):
        before = values[:]
        expected = all_pairs_oracle(values, index_diff, value_diff) if expected is None else expected
        result = Solution().containsNearbyAlmostDuplicate(values, index_diff, value_diff)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_numeric_pair_inequalities(self):
        arrays = 0
        for size in range(6):
            for values in product((-3, -1, 0, 1, 3), repeat=size):
                for index_diff in range(size + 2):
                    for value_diff in range(4):
                        self.check(list(values), index_diff, value_diff)
                arrays += 1
        self.assertEqual(arrays, 3906)

    def test_negative_bucket_boundaries_expiry_and_large_inputs(self):
        self.check([-1, 0], 1, 0, False)
        self.check([-1, 0], 1, 1, True)
        self.check([-3, -1], 1, 1, False)
        self.check([-3, -2], 1, 1, True)
        self.check([1, 5, 9, 1, 5, 9], 2, 3, False)
        self.check([0, 10, 0], 1, 0, False)
        self.check([0, 10, 0], 2, 0, True)
        self.check([-10**9, 10**9], 1, 10**9, False)
        self.check([-10**9, 0], 1, 10**9, True)
        self.check(list(range(0, 200000, 2)), 100000, 1, False)
        self.check([4, 4], 0, 0, False)
        self.check([4, 4], -1, 0, False)
        self.check([4, 4], 1, -1, False)


if __name__ == '__main__':
    unittest.main()
