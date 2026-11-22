import unittest
from itertools import product

from python.p0416_partition_equal_subset_sum import Solution


def subset_sum_oracle(nums):
    total = sum(nums)
    if total % 2:
        return False
    return any(sum(value for index, value in enumerate(nums) if mask & (1 << index)) * 2 == total
               for mask in range(1 << len(nums)))


class EqualPartitionTests(unittest.TestCase):
    def check(self, nums, expected):
        before = nums[:]
        self.assertIs(Solution().canPartition(nums), expected)
        self.assertEqual(nums, before)

    def test_all_small_positive_arrays_against_index_subsets(self):
        checks = 0
        for size in range(7):
            for values in product(range(1, 5), repeat=size):
                self.check(list(values), subset_sum_oracle(values))
                checks += 1
        self.assertEqual(checks, 5461)

    def test_examples_zero_one_usage_and_maximum_contract(self):
        self.check([1, 5, 11, 5], True)
        self.check([1, 2, 3, 5], False)
        self.check([1, 2, 5], False)
        self.check([100], False)
        self.check([], True)
        self.check([100] * 200, True)
        self.check([100] * 199 + [98], False)
        self.check([100] * 199 + [99], False)


if __name__ == '__main__':
    unittest.main()
