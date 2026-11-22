import unittest
from itertools import product

from python.p0930_binary_subarrays_with_sum import Solution


def all_exact_slices(values, target):
    return sum(sum(values[start:end]) == target for start in range(len(values))
               for end in range(start + 1, len(values) + 1))


class ExactBinaryWindowTests(unittest.TestCase):
    def check(self, values, target, expected=None):
        before = values[:]
        if expected is None:
            expected = all_exact_slices(values, target)
        result = Solution().numSubarraysWithSum(values, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_binary_arrays_and_goals_against_slices(self):
        arrays = checks = 0
        for size in range(11):
            for values in product((0, 1), repeat=size):
                arrays += 1
                for target in range(size + 1):
                    self.check(list(values), target)
                    checks += 1
        self.assertEqual((arrays, checks), (2047, 20481))

    def test_maximum_lengths_zero_goal_and_alternating_endpoints(self):
        self.check([0] * 30000, 0, 450015000)
        self.check([1] * 30000, 0, 0)
        self.check([1] * 30000, 10000, 20001)
        self.check([0, 1] * 15000, 0, 15000)
        self.check([0, 1] * 15000, 1, 59998)


if __name__ == '__main__':
    unittest.main()
