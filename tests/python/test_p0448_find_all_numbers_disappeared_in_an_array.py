from itertools import product
import unittest

from python.p0448_find_all_numbers_disappeared_in_an_array import Solution


def set_complement_oracle(nums):
    present = set(nums)
    return [value for value in range(1, len(nums) + 1) if value not in present]


class RestoredSignMarkingTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        actual = Solution().findDisappearedNumbers(nums)
        self.assertIs(type(actual), list)
        self.assertEqual(actual, set_complement_oracle(before) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_every_small_legal_array_against_set_complement(self):
        arrays = 0
        for size in range(1, 7):
            for nums in product(range(1, size + 1), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 50069)
        self.check([], [])

    def test_maximum_length_duplicate_marks_and_repeat_call_restoration(self):
        self.check([1] * 100000, list(range(2, 100001)))
        self.check(list(range(100000, 0, -1)), [])
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        self.check(nums, [5, 6])
        self.check(nums, [5, 6])
        self.check([2, 2], [1])


if __name__ == '__main__':
    unittest.main()
