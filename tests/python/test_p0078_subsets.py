import unittest
from itertools import permutations

from python.p0078_subsets import Solution


def mask_oracle(nums):
    return [tuple(value for index, value in enumerate(nums) if mask & (1 << index))
            for mask in range(1 << len(nums))]


class SubsetTests(unittest.TestCase):
    def check(self, nums):
        before = nums[:]
        actual = Solution().subsets(nums)
        self.assertEqual(sorted(map(tuple, actual)), sorted(mask_oracle(nums)))
        self.assertEqual(len({id(row) for row in actual}), len(actual))
        self.assertTrue(all(row is not nums for row in actual))
        self.assertEqual(nums, before)
        return actual

    def test_all_small_ordered_distinct_inputs_against_bit_masks(self):
        checks = 0
        for size in range(6):
            for values in permutations(range(-2, 3), size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 326)

    def test_empty_maximum_length_and_result_independence(self):
        self.assertEqual(self.check([]), [[]])
        nums = [-10, 10, -4, -3, -2, -1, 0, 1, 2, 3]
        result = self.check(nums)
        self.assertEqual(len(result), 1024)
        position = next(i for i, row in enumerate(result) if row)
        before = [row[:] for row in result]
        result[position][0] = 12345
        for i, row in enumerate(result):
            if i != position:
                self.assertEqual(row, before[i])
        self.assertEqual(nums, [-10, 10, -4, -3, -2, -1, 0, 1, 2, 3])
        self.assertEqual(sorted(map(tuple, self.check([10]))), [(), (10,)])


if __name__ == '__main__':
    unittest.main()
