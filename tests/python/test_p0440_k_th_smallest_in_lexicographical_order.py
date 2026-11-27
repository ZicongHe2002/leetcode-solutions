import unittest

from python.p0440_k_th_smallest_in_lexicographical_order import Solution


class LexicalSubtreeRankTests(unittest.TestCase):
    def check(self, n, k, expected):
        actual = Solution().findKthNumber(n, k)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected)

    def test_every_rank_for_all_small_bounds_against_string_sort(self):
        queries = 0
        for n in range(1, 201):
            expected = sorted(range(1, n + 1), key=str)
            for k, value in enumerate(expected, 1):
                self.check(n, k, value)
                queries += 1
        self.assertEqual(queries, 20100)

    def test_decimal_boundary_clipping_and_maximum_original_bound(self):
        for n in (9, 10, 99, 100, 999, 1000, 9999, 10000):
            expected = sorted(range(1, n + 1), key=str)
            for k in {1, 2, n // 2, n - 1, n}:
                self.check(n, k, expected[k - 1])
        self.check(13, 2, 10)
        self.check(13, 6, 2)
        self.check(10**9, 1, 1)
        self.check(10**9, 2, 10)
        self.check(10**9, 10, 10**9)
        self.check(10**9, 11, 100000001)
        self.check(10**9, 10**9, 999999999)
        self.check(999999999, 999999999, 999999999)


if __name__ == '__main__':
    unittest.main()
