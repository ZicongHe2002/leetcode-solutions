from itertools import combinations_with_replacement
import unittest

from python.p0088_merge_sorted_array import Solution


class MergeSortedArrayTests(unittest.TestCase):
    def test_all_small_sorted_pairs_merge_in_place_and_preserve_second_input(self):
        cases = [
            values
            for length in range(5)
            for values in combinations_with_replacement(range(-1, 2), length)
        ]
        for first in cases:
            for second in cases:
                with self.subTest(first=first, second=second):
                    nums1 = list(first) + [0] * len(second)
                    nums2 = list(second)
                    original_object = nums1
                    returned = Solution().merge(nums1, len(first), nums2, len(second))
                    self.assertIsNone(returned)
                    self.assertIs(nums1, original_object)
                    self.assertEqual(nums1, sorted(first + second))
                    self.assertEqual(nums2, list(second))


if __name__ == "__main__":
    unittest.main()
