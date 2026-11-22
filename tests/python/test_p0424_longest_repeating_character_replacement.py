import unittest
from collections import Counter
from itertools import product

from python.p0424_longest_repeating_character_replacement import Solution


def all_interval_replacement(text, budget):
    best = 0
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            counts = Counter(text[start:end])
            if end - start - max(counts.values()) <= budget:
                best = max(best, end - start)
    return best


class ReplacementWindowTests(unittest.TestCase):
    def check(self, text, budget, expected=None):
        if expected is None:
            expected = all_interval_replacement(text, budget)
        result = Solution().characterReplacement(text, budget)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_ternary_strings_and_budgets_against_all_intervals(self):
        arrays = checks = 0
        for size in range(8):
            for letters in product('ABC', repeat=size):
                text = ''.join(letters)
                arrays += 1
                for budget in range(size + 1):
                    self.check(text, budget)
                    checks += 1
        self.assertEqual((arrays, checks), (3280, 24604))

    def test_maximum_lengths_zero_and_half_budget(self):
        self.check('A' * 100000, 0, 100000)
        self.check('AB' * 50000, 0, 1)
        self.check('AB' * 50000, 50000, 100000)
        self.check('AABABBA', 1, 4)


if __name__ == '__main__':
    unittest.main()
