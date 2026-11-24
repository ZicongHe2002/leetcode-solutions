import unittest
from itertools import combinations

from python.p0033_rotated_search import Solution


class RotatedSearchTests(unittest.TestCase):
    def check(self, values, target, expected):
        before = values[:]
        self.assertEqual(Solution().search(values, target), expected)
        self.assertEqual(values, before)

    def test_all_small_distinct_subsets_and_rotations(self):
        rotations = queries = 0
        for size in range(1, 8):
            for subset in combinations(range(-3, 4), size):
                for offset in range(size):
                    values = list(subset[offset:] + subset[:offset])
                    rotations += 1
                    for target in range(-4, 5):
                        expected = next((index for index, value in enumerate(values) if value == target), -1)
                        self.check(values, target, expected)
                        queries += 1
        self.assertEqual((rotations, queries), (448, 4032))

    def test_examples_empty_extension_and_maximum_length(self):
        for values, target, expected in [([4, 5, 6, 7, 0, 1, 2], 0, 4), ([4, 5, 6, 7, 0, 1, 2], 3, -1),
                                        ([1], 1, 0), ([1], 0, -1), ([3, 1], 1, 1), ([1, 3], 3, 1),
                                        ([-10000, 0, 10000], 10000, 2), ([10000, -10000, 0], -10000, 1)]:
            self.check(values, target, expected)
        self.check([], 0, -1)
        values = list(range(-2500, 2500))
        values = values[1234:] + values[:1234]
        for target in range(-2501, 2501):
            expected = (target + 2500 - 1234) % 5000 if -2500 <= target < 2500 else -1
            self.check(values, target, expected)


if __name__ == '__main__':
    unittest.main()
