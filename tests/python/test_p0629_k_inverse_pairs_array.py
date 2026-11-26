import unittest
from itertools import permutations
from math import comb

from python.p0629_k_inverse_pairs_array import Solution


MODULUS = 10**9 + 7


def exact_polynomial_rows(limit):
    rows = {1: [1]}
    for size in range(2, limit + 1):
        row = [0] * (size * (size - 1) // 2 + 1)
        for degree, coefficient in enumerate(rows[size - 1]):
            for inserted_inversions in range(size):
                row[degree + inserted_inversions] += coefficient
        rows[size] = row
    return rows


def pentagonal_coefficient(n, k):
    assert 0 <= k <= n
    coefficient = comb(n + k - 1, k)
    index = 1
    while index * (3 * index - 1) // 2 <= k:
        sign = -1 if index % 2 else 1
        for degree in (index * (3 * index - 1) // 2,
                       index * (3 * index + 1) // 2):
            if degree <= k:
                coefficient += sign * comb(n + k - degree - 1, k - degree)
        index += 1
    return coefficient % MODULUS


class InversePairTests(unittest.TestCase):
    def check(self, n, k, expected):
        actual = Solution().kInversePairs(n, k)
        self.assertIs(type(actual), int)
        self.assertGreaterEqual(actual, 0)
        self.assertLess(actual, MODULUS)
        self.assertEqual(actual, expected, (n, k))

    def test_all_small_permutations_by_direct_pair_count(self):
        count = queries = 0
        for n in range(1, 9):
            maximum = n * (n - 1) // 2
            histogram = [0] * (maximum + 3)
            for values in permutations(range(1, n + 1)):
                inversions = sum(values[left] > values[right]
                                 for left in range(n)
                                 for right in range(left + 1, n))
                histogram[inversions] += 1
                count += 1
            for k, expected in enumerate(histogram):
                self.check(n, k, expected)
                queries += 1
        self.assertEqual((count, queries), (46233, 108))

    def test_exact_unreduced_polynomial_convolution(self):
        rows = exact_polynomial_rows(60)
        for n in (10, 20, 30, 50, 60):
            maximum = n * (n - 1) // 2
            for k in sorted({0, 1, 5, 100, 500, 1000, min(maximum, 1000)}):
                expected = rows[n][k] if k <= maximum else 0
                self.check(n, k, expected % MODULUS)
        self.assertGreater(rows[60][500], MODULUS)
        self.check(1, 1000, 0)

    def test_maximum_n_and_k_against_generating_function(self):
        for k in (0, 1, 2, 999, 1000):
            self.check(1000, k, pentagonal_coefficient(1000, k))
        self.assertEqual(pentagonal_coefficient(1000, 1), 999)


if __name__ == '__main__':
    unittest.main()
