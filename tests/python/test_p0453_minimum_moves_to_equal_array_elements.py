from collections import deque
from itertools import product
import unittest

from python.p0453_minimum_moves_to_equal_array_elements import Solution


def normalized(values):
    ordered = sorted(values)
    return tuple(value - ordered[0] for value in ordered)


def original_increment_bfs(nums):
    start = normalized(nums)
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        state, distance = queue.popleft()
        if state[-1] == 0:
            return distance
        for skipped in range(len(state)):
            changed = normalized([value + (index != skipped) for index, value in enumerate(state)])
            if changed not in seen:
                seen.add(changed)
                queue.append((changed, distance + 1))
    raise AssertionError('finite integer array must be equalizable')


class EqualizeRelativeMovesTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        actual = Solution().minMoves(nums)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, original_increment_bfs(nums) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_all_small_signed_arrays_against_actual_increment_operations(self):
        arrays = 0
        for size in range(1, 5):
            for nums in product((-1, 0, 2), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 120)

    def test_maximum_length_value_bounds_and_large_intermediate_sum(self):
        self.check([1, 2, 3], 3)
        self.check([-10**9, 10**9], 2 * 10**9)
        self.check([-10**9] * 100000, 0)
        self.check([0] + [10000] * 99999, 999990000)
        self.check([10**9], 0)
        self.check([7, 7, 7], 0)


if __name__ == '__main__':
    unittest.main()
