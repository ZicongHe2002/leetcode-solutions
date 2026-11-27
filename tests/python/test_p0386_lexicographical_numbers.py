import unittest

from python.p0386_lexicographical_numbers import Solution


class LexicalPrefixTraversalTests(unittest.TestCase):
    def check(self, n):
        actual = Solution().lexicalOrder(n)
        self.assertIs(type(actual), list)
        self.assertEqual(actual, sorted(range(1, n + 1), key=str))
        self.assertEqual(len(actual), n)
        self.assertEqual(set(actual), set(range(1, n + 1)))
        self.assertTrue(all(type(value) is int for value in actual))

    def test_every_small_bound_against_direct_string_sort(self):
        for n in range(501):
            self.check(n)

    def test_decimal_prefix_backtracking_and_maximum_bound(self):
        for n in (9, 10, 11, 19, 20, 99, 100, 109, 199, 999, 1000, 9999, 10000, 49999, 50000):
            self.check(n)
        self.assertEqual(Solution().lexicalOrder(13), [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
