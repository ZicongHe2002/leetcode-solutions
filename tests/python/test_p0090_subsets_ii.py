import unittest
from itertools import product

from python.p0090_subsets_ii import Solution


def index_mask_oracle(nums):
    return {tuple(sorted(value for index, value in enumerate(nums) if mask & (1 << index)))
            for mask in range(1 << len(nums))}


class DuplicateSubsetTests(unittest.TestCase):
    def check(self, nums):
        before = nums[:]
        actual = Solution().subsetsWithDup(nums)
        self.assertEqual(sorted(map(tuple, actual)), sorted(index_mask_oracle(nums)))
        self.assertEqual(nums, before)
        self.assertEqual(len({id(row) for row in actual}), len(actual))
        self.assertTrue(all(row is not nums and row == sorted(row) for row in actual))
        return actual

    def test_all_small_ordered_arrays_against_index_masks(self):
        checks = 0
        for size in range(8):
            for nums in product(range(-1, 2), repeat=size):
                self.check(list(nums))
                checks += 1
        self.assertEqual(checks, 3280)

    def test_maximum_length_duplicate_counts_and_empty_extension(self):
        self.assertEqual(len(self.check(list(range(-5, 5)))), 1024)
        self.assertEqual(len(self.check([5] * 10)), 11)
        self.assertEqual(len(self.check([-10] * 5 + [10] * 5)), 36)
        self.assertEqual(self.check([]), [[]])
        self.assertEqual(sorted(map(tuple, self.check([1, 2, 2]))),
                         [(), (1,), (1, 2), (1, 2, 2), (2,), (2, 2)])


if __name__ == '__main__':
    unittest.main()
