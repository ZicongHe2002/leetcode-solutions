import unittest
from functools import lru_cache
from itertools import product

from python.p0740_delete_and_earn import Solution


@lru_cache(None)
def all_deletion_orders(remaining):
    best = 0
    for index, value in enumerate(remaining):
        rest = tuple(other for position, other in enumerate(remaining)
                     if position != index and abs(other - value) != 1)
        best = max(best, value + all_deletion_orders(rest))
    return best


class DeleteEarnTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        if expected is None:
            expected = all_deletion_orders(tuple(sorted(nums)))
        result = Solution().deleteAndEarn(nums)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(nums, before)

    def test_all_small_positive_arrays_against_actual_deletion_orders(self):
        checks = 0
        for size in range(1, 8):
            for values in product((1, 2, 3), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_length_value_domain_duplicate_groups_and_adjacent_conflicts(self):
        self.check([10000] * 20000, 200000000)
        self.check(list(range(10000, 0, -1)) * 2, 50010000)
        self.check([1, 2] * 10000, 20000)
        self.check([1, 1, 1, 2, 4, 5, 5, 5, 6])
        self.check([1, 10000], 10001)
        self.check([1], 1)


if __name__ == '__main__':
    unittest.main()
