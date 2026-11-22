import unittest
from collections import deque
from itertools import product

from python.p0045_jump_game_ii import Solution


def shortest_path_oracle(nums):
    if not nums:
        return -1
    distance = [-1] * len(nums)
    distance[0] = 0
    pending = deque([0])
    while pending:
        index = pending.popleft()
        for target in range(index + 1, min(len(nums), index + nums[index] + 1)):
            if distance[target] == -1:
                distance[target] = distance[index] + 1
                pending.append(target)
    return distance[-1]


class MinimumJumpTests(unittest.TestCase):
    def check(self, nums, expected):
        before = nums[:]
        self.assertEqual(Solution().jump(nums), expected)
        self.assertEqual(nums, before)

    def test_small_reachable_contract_and_unreachable_extension_against_bfs(self):
        checks = reachable = unreachable = 0
        for size in range(1, 8):
            for values in product(range(4), repeat=size):
                expected = shortest_path_oracle(values)
                self.check(list(values), expected)
                reachable += expected >= 0
                unreachable += expected < 0
                checks += 1
        self.assertEqual(checks, 21844)
        self.assertGreater(reachable, 0)
        self.assertGreater(unreachable, 0)

    def test_examples_maximum_reachable_contract_and_separate_extensions(self):
        self.check([2, 3, 1, 1, 4], 2)
        self.check([2, 3, 0, 1, 4], 2)
        self.check([0], 0)
        self.check([1] * 10000, 9999)
        self.check([1000] * 10000, 10)
        self.check([0, 1], -1)
        self.check([], -1)


if __name__ == '__main__':
    unittest.main()
