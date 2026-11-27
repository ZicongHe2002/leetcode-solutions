from itertools import product
import unittest

from python.p0421_maximum_xor_of_two_numbers_in_an_array import Solution


def every_index_pair_oracle(nums):
    return max((nums[first] ^ nums[second] for first in range(len(nums))
                for second in range(first, len(nums))), default=0)


class MaximumXorPrefixTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        actual = Solution().findMaximumXOR(nums)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, every_index_pair_oracle(nums) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_all_small_arrays_against_every_index_pair(self):
        arrays = 0
        for size in range(8):
            for nums in product((0, 1, 2, 7), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 21845)

    def test_maximum_length_highest_bit_duplicates_and_singletons(self):
        self.check([3, 10, 5, 25, 2, 8], 28)
        self.check([2**31 - 1], 0)
        self.check([2**31 - 1] * 20, 0)
        self.check([0, 2**31 - 1], 2**31 - 1)
        self.check(list(range(200000)), 2**18 - 1)
        self.check([0] * 199999 + [2**31 - 1], 2**31 - 1)


if __name__ == '__main__':
    unittest.main()
