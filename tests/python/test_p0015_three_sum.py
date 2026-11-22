import unittest
from itertools import combinations, product

from python.p0015_three_sum import Solution


class ThreeSumTests(unittest.TestCase):
    def check(self, values, expected):
        before = values[:]
        actual = Solution().threeSum(values)
        self.assertEqual(sorted(tuple(sorted(group)) for group in actual), sorted(expected))
        self.assertEqual(values, before)

    def test_small_arrays_against_all_index_triples(self):
        checked = 0
        for size in range(3, 7):
            for values in product(range(-2, 3), repeat=size):
                expected = {tuple(sorted(triple)) for triple in combinations(values, 3) if sum(triple) == 0}
                self.check(list(values), expected)
                checked += 1
        self.assertEqual(checked, 19500)

    def test_duplicates_short_extensions_and_length_boundaries(self):
        self.check([-1, 0, 1, 2, -1, -4], {(-1, -1, 2), (-1, 0, 1)})
        self.check([-100000, 0, 100000], {(-100000, 0, 100000)})
        for values in ([], [0], [0, 0]):
            self.check(values, set())
        self.check([0] * 3000, {(0, 0, 0)})
        self.check(list(range(1, 3001)), set())


if __name__ == '__main__':
    unittest.main()
