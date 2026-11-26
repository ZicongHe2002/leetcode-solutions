from itertools import product
import unittest

from python.p0474_ones_and_zeroes import Solution


def index_subset_oracle(strings, zero_budget, one_budget):
    best = 0
    for mask in range(1 << len(strings)):
        chosen = [text for index, text in enumerate(strings) if mask & (1 << index)]
        if sum(text.count('0') for text in chosen) <= zero_budget and sum(text.count('1') for text in chosen) <= one_budget:
            best = max(best, len(chosen))
    return best


class BinaryBudgetKnapsackTests(unittest.TestCase):
    def check(self, strings, m, n, expected=None):
        before = strings[:]
        actual = Solution().findMaxForm(strings, m, n)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, index_subset_oracle(strings, m, n) if expected is None else expected)
        self.assertEqual(strings, before)

    def test_all_small_lists_and_budgets_against_index_subsets(self):
        arrays = queries = 0
        for size in range(5):
            for strings in product(('0', '1', '00', '01', '11'), repeat=size):
                arrays += 1
                for m, n in product(range(4), repeat=2):
                    self.check(list(strings), m, n)
                    queries += 1
        self.assertEqual((arrays, queries), (781, 12496))

    def test_maximum_count_length_budget_and_zero_cost_dimension(self):
        self.check(['0'] * 300 + ['1'] * 300, 100, 100, 200)
        self.check(['0' * 100] * 300 + ['1' * 100] * 300, 100, 100, 2)
        self.check(['01' * 50] * 600, 100, 100, 2)
        self.check(['0'], 100, 100, 1)
        self.check(['1'], 100, 100, 1)
        self.check(['10', '0001', '111001', '1', '0'], 5, 3, 4)
        self.check(['0', '0', '0'], 2, 0, 2)
        self.check(['1', '1', '1'], 0, 2, 2)


if __name__ == '__main__':
    unittest.main()
