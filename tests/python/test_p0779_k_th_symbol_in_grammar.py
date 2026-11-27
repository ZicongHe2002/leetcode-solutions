import random
import unittest

from python.p0779_k_th_symbol_in_grammar import Solution


def parent_symbol(n, k):
    if n == 1:
        return 0
    parent = parent_symbol(n - 1, (k + 1) // 2)
    return parent if k % 2 else 1 - parent


class KthGrammarTests(unittest.TestCase):
    def check(self, n, k, expected):
        result = Solution().kthGrammar(n, k)
        self.assertIs(type(result), int)
        self.assertIn(result, (0,1))
        self.assertEqual(result, expected, (n,k))

    def test_every_symbol_in_twelve_explicitly_rewritten_rows(self):
        row, checked = '0', 0
        for n in range(1, 13):
            for k, symbol in enumerate(row, 1):
                self.check(n, k, int(symbol))
                checked += 1
            row = ''.join('01' if symbol == '0' else '10' for symbol in row)
        self.assertEqual(checked, 4095)

    def test_seeded_large_parent_paths_row_limits_and_power_boundaries(self):
        rng = random.Random(779)
        for _ in range(1000):
            n = rng.randrange(1, 31)
            k = rng.randrange(1, (1 << (n - 1)) + 1)
            self.check(n, k, parent_symbol(n, k))
        self.check(1, 1, 0)
        self.check(2, 1, 0)
        self.check(2, 2, 1)
        self.check(30, 1, 0)
        self.check(30, 1 << 29, 1)
        for bit in range(1, 30):
            self.check(30, 1 << bit, bit % 2)
        for bit in range(29):
            self.check(30, (1 << bit) + 1, 1)


if __name__ == '__main__':
    unittest.main()
