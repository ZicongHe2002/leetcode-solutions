import unittest
from collections import deque
from itertools import product

from python.p0055_jump_game import Solution


def explicit_graph_oracle(nums):
    if not nums:
        return False
    pending = deque([0])
    visited = {0}
    while pending:
        index = pending.popleft()
        if index == len(nums) - 1:
            return True
        for target in range(index + 1, min(len(nums), index + nums[index] + 1)):
            if target not in visited:
                visited.add(target)
                pending.append(target)
    return False


class JumpReachabilityTests(unittest.TestCase):
    def check(self, nums, expected):
        before = nums[:]
        self.assertIs(Solution().canJump(nums), expected)
        self.assertEqual(nums, before)

    def test_all_small_jump_arrays_against_explicit_graph_bfs(self):
        checks = 0
        for size in range(1, 8):
            for values in product(range(4), repeat=size):
                self.check(list(values), explicit_graph_oracle(values))
                checks += 1
        self.assertEqual(checks, 21844)

    def test_examples_singletons_maximum_length_and_empty_extension(self):
        self.check([2, 3, 1, 1, 4], True)
        self.check([3, 2, 1, 0, 4], False)
        self.check([0], True)
        self.check([1] * 10000, True)
        self.check([1] * 9998 + [0, 0], False)
        self.check([100000] + [0] * 9999, True)
        self.check([], False)


if __name__ == '__main__':
    unittest.main()
