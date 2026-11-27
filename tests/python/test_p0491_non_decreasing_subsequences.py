from itertools import product
import unittest

from python.p0491_non_decreasing_subsequences import Solution


def ordered_index_subset_oracle(nums):
    result = set()
    for mask in range(1 << len(nums)):
        candidate = tuple(value for index, value in enumerate(nums) if mask & (1 << index))
        if len(candidate) >= 2 and all(left <= right for left, right in zip(candidate, candidate[1:])):
            result.add(candidate)
    return result


class LocalValueDeduplicationTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        actual = Solution().findSubsequences(nums)
        self.assertIs(type(actual), list)
        self.assertTrue(all(type(sequence) is list for sequence in actual))
        distinct = {tuple(sequence) for sequence in actual}
        self.assertEqual(len(actual), len(distinct))
        self.assertEqual(distinct, ordered_index_subset_oracle(nums) if expected is None else expected)
        self.assertEqual(nums, before)
        return len(actual)

    def test_all_small_signed_arrays_against_every_ordered_index_subset(self):
        arrays = 0
        for size in range(8):
            for nums in product((-1, 0, 1), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 3280)

    def test_maximum_length_output_size_equal_values_descents_and_value_limits(self):
        self.assertEqual(self.check(list(range(-7, 8))), (1 << 15) - 16)
        self.check([100] * 15, {tuple([100] * size) for size in range(2, 16)})
        self.check([-100] * 15, {tuple([-100] * size) for size in range(2, 16)})
        self.check(list(range(15, 0, -1)), set())
        self.check([-100, 100, -100, 100])
        self.check([4, 6, 7, 7])


if __name__ == '__main__':
    unittest.main()
