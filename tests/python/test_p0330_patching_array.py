from collections import deque
from itertools import combinations_with_replacement
import unittest

from python.p0330_patching_array import Solution


def all_patch_sequences_bfs(nums, target):
    mask = (1 << (target + 1)) - 1
    reachable = 1
    for value in nums:
        reachable = (reachable | (reachable << value)) & mask
    queue = deque([(reachable, 0)])
    seen = {reachable}
    while queue:
        current, count = queue.popleft()
        if current == mask:
            return count
        for patch in range(1, target + 1):
            changed = (current | (current << patch)) & mask
            if changed not in seen:
                seen.add(changed)
                queue.append((changed, count + 1))
    raise AssertionError('adding enough ones must cover the target')


class MinimumPatchCoverageTests(unittest.TestCase):
    def check(self, nums, n, expected=None):
        before = nums[:]
        actual = Solution().minPatches(nums, n)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, all_patch_sequences_bfs(nums, n) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_small_sorted_arrays_against_all_patch_choices_bfs(self):
        arrays = queries = 0
        for size in range(5):
            for nums in combinations_with_replacement(range(1, 7), size):
                arrays += 1
                for n in range(1, 11):
                    self.check(list(nums), n)
                    queries += 1
        self.assertEqual((arrays, queries), (210, 2100))

    def test_large_target_duplicate_values_and_maximum_array_length(self):
        self.check([], 2**31 - 1, 31)
        self.check([1], 2**31 - 1, 30)
        self.check([1, 3], 6, 1)
        self.check([1, 5, 10], 20, 2)
        self.check([1, 2, 2], 5, 0)
        self.check([10000] * 1000, 10000, 14)
        self.check(list(range(1, 1001)), 500500, 0)
        self.check(list(range(1, 1001)), 2**31 - 1, 13)


if __name__ == '__main__':
    unittest.main()
