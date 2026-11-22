import unittest
from itertools import combinations_with_replacement

from python.p0040_combination_sum_ii import Solution


def index_subset_oracle(candidates, target):
    answers = set()
    for mask in range(1 << len(candidates)):
        selected = [value for index, value in enumerate(candidates) if mask & (1 << index)]
        if sum(selected) == target:
            answers.add(tuple(sorted(selected)))
    return answers


class SingleUseCombinationTests(unittest.TestCase):
    def check(self, candidates, target, expected=None):
        before = candidates[:]
        if expected is None:
            expected = index_subset_oracle(candidates, target)
        actual = Solution().combinationSum2(candidates, target)
        self.assertEqual(sorted(map(tuple, actual)), sorted(expected))
        self.assertEqual(candidates, before)
        self.assertEqual(len({id(row) for row in actual}), len(actual))
        self.assertTrue(all(row is not candidates and row == sorted(row) for row in actual))

    def test_all_small_multisets_and_targets_against_index_subsets(self):
        checks = 0
        for size in range(1, 7):
            for values in combinations_with_replacement(range(1, 5), size):
                for target in range(1, 13):
                    self.check(list(values if target % 2 else values[::-1]), target)
                    checks += 1
        self.assertEqual(checks, 2508)

    def test_duplicate_counts_maximum_length_and_empty_extensions(self):
        self.check([10, 1, 2, 7, 6, 1, 5], 8, [(1, 1, 6), (1, 2, 5), (1, 7), (2, 6)])
        self.check([1] * 100, 30, [(1,) * 30])
        self.check([50] * 100, 30, [])
        self.check([1, 1, 2, 2], 4, [(1, 1, 2), (2, 2)])
        self.check([], 1)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
