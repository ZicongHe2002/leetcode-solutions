from itertools import combinations_with_replacement
import unittest

from python.p0026_remove_duplicates_from_sorted_array import Solution


class RemoveDuplicatesTests(unittest.TestCase):
    def test_sorted_inputs_have_exact_distinct_prefix_in_same_array(self):
        for length in range(9):
            for values in combinations_with_replacement(range(-2, 3), length):
                with self.subTest(values=values):
                    nums = list(values)
                    original_object = nums
                    expected = sorted(set(values))
                    count = Solution().removeDuplicates(nums)
                    self.assertEqual(count, len(expected))
                    self.assertEqual(nums[:count], expected)
                    self.assertIs(nums, original_object)
                    self.assertEqual(len(nums), length)


if __name__ == "__main__":
    unittest.main()
