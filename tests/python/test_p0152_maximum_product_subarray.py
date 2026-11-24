import math
import unittest
from itertools import product

from python.p0152_maximum_product_subarray import Solution


def interval_oracle(nums):
    return max(math.prod(nums[left:right]) for left in range(len(nums))
               for right in range(left + 1, len(nums) + 1))


class ProductSubarrayTests(unittest.TestCase):
    def check(self, nums, expected):
        before = nums[:]
        self.assertEqual(Solution().maxProduct(nums), expected)
        self.assertEqual(nums, before)

    def test_all_small_arrays_against_complete_interval_products(self):
        checks = 0
        for size in range(1, 7):
            for values in product(range(-2, 3), repeat=size):
                self.check(list(values), interval_oracle(values))
                checks += 1
        self.assertEqual(checks, 19530)

    def test_examples_sign_changes_and_maximum_contract(self):
        self.check([2, 3, -2, 4], 6)
        self.check([-2, 0, -1], 0)
        self.check([-2, 3, -4], 24)
        self.check([1] * 20000, 1)
        self.check([0] * 20000, 0)
        self.check([-1] * 20000, 1)
        self.check([10] * 9, 10**9)
        self.check([10] * 9 + [0] + [-10] * 9, 10**9)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
