from itertools import product
import unittest

from python.p0477_total_hamming_distance import Solution


def all_xor_pairs(nums):
    return sum((nums[left] ^ nums[right]).bit_count()
               for left in range(len(nums)) for right in range(left + 1, len(nums)))


class HammingBitPairCountTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        actual = Solution().totalHammingDistance(nums)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, all_xor_pairs(nums) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_all_small_arrays_against_explicit_xor_pairs(self):
        arrays = 0
        for size in range(7):
            for nums in product((0, 1, 2, 3, 7), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 19531)

    def test_maximum_length_value_zero_and_equal_group_pair_count(self):
        self.check([0] * 5000 + [10**9] * 5000, 25000000 * (10**9).bit_count())
        self.check([10**9] * 10000, 0)
        self.check([0] * 10000, 0)
        self.check([0, (1 << 29) - 1], 29)
        self.check([0, 10**9], (10**9).bit_count())
        self.check([4, 14, 2], 6)
        self.check([1], 0)


if __name__ == '__main__':
    unittest.main()
