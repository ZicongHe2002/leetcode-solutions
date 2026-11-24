import unittest
from itertools import product

from python.p0213_house_robber_ii import Solution


def circular_mask_oracle(nums):
    best = 0
    for mask in range(1 << len(nums)):
        if len(nums) > 1 and any(mask & (1 << index) and mask & (1 << ((index + 1) % len(nums)))
                                 for index in range(len(nums))):
            continue
        best = max(best, sum(value for index, value in enumerate(nums) if mask & (1 << index)))
    return best


class CircularRobberTests(unittest.TestCase):
    def check(self, nums, expected):
        before = nums[:]
        self.assertEqual(Solution().rob(nums), expected)
        self.assertEqual(nums, before)

    def test_all_small_circular_arrays_against_legal_masks(self):
        checks = 0
        for size in range(7):
            for values in product(range(4), repeat=size):
                self.check(list(values), circular_mask_oracle(values))
                checks += 1
        self.assertEqual(checks, 5461)

    def test_singletons_endpoints_examples_and_maximum_contract(self):
        self.check([2, 3, 2], 3)
        self.check([1, 2, 3, 1], 4)
        self.check([1000], 1000)
        self.check([1000, 1000], 1000)
        self.check([1000] * 100, 50000)
        self.check([1000] * 99, 49000)
        self.check([1000, 0] * 50, 50000)
        self.check([0], 0)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
