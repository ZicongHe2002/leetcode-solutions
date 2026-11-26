from math import comb
import unittest

from python.p0509_fibonacci_number import Solution


def tiling_combination_oracle(n):
    if n == 0:
        return 0
    cells = n - 1
    return sum(comb(cells - doubles, doubles) for doubles in range(cells // 2 + 1))


class BinaryPrefixFibonacciTests(unittest.TestCase):
    def test_entire_original_domain_against_independent_tiling_counts(self):
        results = []
        for n in range(31):
            actual = Solution().fib(n)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, tiling_combination_oracle(n))
            results.append(actual)
        self.assertEqual(len(results), 31)
        self.assertEqual(results[:3], [0, 1, 1])
        self.assertEqual(results[-1], 832040)


if __name__ == '__main__':
    unittest.main()
