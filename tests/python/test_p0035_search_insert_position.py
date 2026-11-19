import unittest

from python.p0035_search_insert_position import Solution


class SearchInsertTests(unittest.TestCase):
    def test_all_small_subsets_match_linear_insertion_boundary(self):
        for mask in range(128):
            values = [bit - 3 for bit in range(7) if mask & (1 << bit)]
            for target in range(-4, 5):
                with self.subTest(values=values, target=target):
                    nums = values.copy()
                    position = Solution().searchInsert(nums, target)
                    self.assertEqual(position, sum(value < target for value in values))
                    self.assertEqual(nums, values)
                    inserted = values[:position] + [target] + values[position:]
                    self.assertEqual(inserted, sorted(inserted))


if __name__ == "__main__":
    unittest.main()
