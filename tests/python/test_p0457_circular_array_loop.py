from itertools import product
import unittest

from python.p0457_circular_array_loop import Solution


def recorded_path_oracle(nums):
    for start in range(len(nums)):
        positive = nums[start] > 0
        current, positions = start, {}
        while (nums[current] > 0) == positive:
            if current in positions:
                if len(positions) - positions[current] > 1:
                    return True
                break
            positions[current] = len(positions)
            current = (current + nums[current]) % len(nums)
    return False


class DirectedCircularLoopTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        expected = recorded_path_oracle(before) if expected is None else expected
        actual = Solution().circularArrayLoop(nums)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, expected)
        self.assertTrue(all(after == 0 or after == original for after, original in zip(nums, before)))

    def test_all_small_nonzero_arrays_against_explicit_path_records(self):
        arrays = 0
        for size in range(8):
            for nums in product((-2, -1, 1, 2), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 21845)

    def test_maximum_length_direction_changes_and_full_modulo_steps(self):
        self.check([1] * 5000, True)
        self.check([-1] * 5000, True)
        self.check([1] * 4999 + [-1], False)
        self.check([1000] * 1000, False)
        self.check([-1000] * 1000, False)
        self.check([1000] * 5000, True)
        self.check([2, -1, 1, 2, 2], True)
        self.check([1, -1], False)


if __name__ == '__main__':
    unittest.main()
