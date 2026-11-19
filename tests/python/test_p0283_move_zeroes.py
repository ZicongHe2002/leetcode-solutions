from itertools import product
import unittest

from python.p0283_move_zeroes import Solution


class MoveZeroesTests(unittest.TestCase):
    def test_small_arrays_keep_nonzero_order_and_all_original_zeroes(self):
        for length in range(8):
            for values in product((-1, 0, 2), repeat=length):
                with self.subTest(values=values):
                    nums = list(values)
                    original_object = nums
                    expected = [value for value in values if value != 0]
                    expected += [0] * values.count(0)
                    returned = Solution().moveZeroes(nums)
                    self.assertIsNone(returned)
                    self.assertIs(nums, original_object)
                    self.assertEqual(nums, expected)
                    self.assertEqual(len(nums), length)


if __name__ == "__main__":
    unittest.main()
