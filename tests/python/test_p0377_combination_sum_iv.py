import unittest
from itertools import combinations, permutations, product
from math import comb

from python.p0377_combination_sum_iv import Solution


def explicit_sequence_count(nums, target):
    return sum(sum(sequence) == target
               for length in range(target // min(nums) + 1)
               for sequence in product(nums, repeat=length))


class OrderedCombinationTests(unittest.TestCase):
    def check(self, nums, target, expected=None):
        before = nums[:]
        if expected is None:
            expected = explicit_sequence_count(nums, target)
        result = Solution().combinationSum4(nums, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(nums, before)

    def test_all_small_candidate_subsets_orders_and_targets_against_tuples(self):
        checks = 0
        for size in range(1, 6):
            for values in combinations(range(1, 6), size):
                for order in permutations(values):
                    for target in range(7):
                        self.check(list(order), target)
                        checks += 1
        self.assertEqual(checks, 2275)

    def test_maximum_target_candidate_count_and_large_representable_answer(self):
        self.check([1], 1000, 1)
        self.check([1000], 1000, 1)
        self.check([999], 1000, 0)
        self.check(list(range(801, 1001)), 1000, 1)
        expected = sum(comb(45 - twos, twos) for twos in range(23))
        self.assertEqual(expected, 1836311903)
        self.check([1, 2], 45, expected)


if __name__ == '__main__':
    unittest.main()
