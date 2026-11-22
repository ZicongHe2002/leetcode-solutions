import unittest
from itertools import permutations

from python.p0046_permutations import Solution


class PermutationTests(unittest.TestCase):
    def check(self, nums):
        before = nums[:]
        actual = Solution().permute(nums)
        expected = list(permutations(nums))
        self.assertEqual(sorted(map(tuple, actual)), sorted(expected))
        self.assertEqual(len({id(row) for row in actual}), len(actual))
        self.assertTrue(all(row is not nums for row in actual))
        self.assertTrue(all(len(row) == len(nums) and sorted(row) == sorted(nums) for row in actual))
        self.assertEqual(nums, before)
        return actual

    def test_all_small_ordered_distinct_inputs_against_library_oracle(self):
        checks = 0
        for size in range(1, 6):
            for values in permutations(range(-2, 3), size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 325)

    def test_empty_maximum_length_and_result_independence(self):
        self.assertEqual(self.check([]), [[]])
        nums = [-10, 10, 0, -1, 1, 2]
        result = self.check(nums)
        self.assertEqual(len(result), 720)
        other = result[1][:]
        result[0][0] = 12345
        self.assertEqual(result[1], other)
        self.assertEqual(nums, [-10, 10, 0, -1, 1, 2])
        self.assertEqual(self.check([10]), [[10]])


if __name__ == '__main__':
    unittest.main()
