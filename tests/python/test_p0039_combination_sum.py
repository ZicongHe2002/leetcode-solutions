import unittest
from itertools import combinations, product

from python.p0039_combination_sum import Solution


def count_vector_oracle(candidates, target):
    values = sorted(candidates)
    answers = []
    for counts in product(*(range(target // value + 1) for value in values)):
        if sum(value * count for value, count in zip(values, counts)) == target:
            answers.append(tuple(value for value, count in zip(values, counts) for _ in range(count)))
    return answers


class CombinationSumTests(unittest.TestCase):
    def check(self, candidates, target):
        before = candidates[:]
        actual = Solution().combinationSum(candidates, target)
        self.assertEqual(sorted(map(tuple, actual)), sorted(count_vector_oracle(candidates, target)))
        self.assertEqual(candidates, before)
        self.assertEqual(len({id(row) for row in actual}), len(actual))
        self.assertTrue(all(row is not candidates and row == sorted(row) for row in actual))
        return actual

    def test_all_small_candidate_sets_and_targets_against_counts(self):
        checks = 0
        for size in range(1, 5):
            for values in combinations(range(2, 8), size):
                for target in range(1, 16):
                    self.check(list(values if target % 2 else values[::-1]), target)
                    checks += 1
        self.assertEqual(checks, 840)

    def test_examples_maximum_contract_and_empty_extensions(self):
        self.assertEqual(sorted(map(tuple, self.check([2, 3, 6, 7], 7))), [(2, 2, 3), (7,)])
        self.check([5, 2, 3], 40)
        self.check(list(range(11, 41)), 10)
        self.assertEqual(self.check([40], 40), [[40]])
        self.assertEqual(self.check([2], 1), [])
        self.assertEqual(self.check([], 1), [])
        self.assertEqual(self.check([], 0), [[]])
        self.assertEqual(self.check([1], 4), [[1, 1, 1, 1]])


if __name__ == '__main__':
    unittest.main()
