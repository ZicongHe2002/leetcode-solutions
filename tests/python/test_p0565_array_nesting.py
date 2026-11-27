from itertools import permutations
import unittest

from python.p0565_array_nesting import Solution


def independent_sets(nums):
    best = 0
    for start in range(len(nums)):
        values = set()
        current = nums[start]
        while current not in values:
            values.add(current)
            current = nums[current]
        best = max(best, len(values))
    return best


class ArrayNestingTests(unittest.TestCase):
    def check(self, nums, expected):
        before = nums[:]
        result = Solution().arrayNesting(nums)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(nums, before)

    def test_all_permutations_through_eight_against_per_start_sets(self):
        checks = 0
        for size in range(1, 9):
            for values in permutations(range(size)):
                nums = list(values)
                self.check(nums, independent_sets(nums))
                checks += 1
        self.assertEqual(checks, 46233)

    def test_hundred_thousand_elements_and_disjoint_cycle_lengths(self):
        self.check(list(range(1, 100000)) + [0], 100000)
        self.check(list(range(100000)), 1)
        self.check([index ^ 1 for index in range(100000)], 2)
        self.check([1, 0, 3, 4, 2, 5], 3)
        self.check([5, 4, 0, 3, 1, 6, 2], 4)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
