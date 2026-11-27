from collections import Counter
from itertools import combinations_with_replacement
import unittest

from python.p0080_remove_duplicates_from_sorted_array_ii import Solution


class AtMostTwiceCounterOracleTests(unittest.TestCase):
    def check(self, values):
        frequencies = Counter(values)
        expected = [value for value in sorted(frequencies)
                    for _ in range(min(2, frequencies[value]))]
        result = Solution().removeDuplicates(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, len(expected))
        self.assertEqual(values[:result], expected)

    def test_every_small_sorted_array_against_frequency_counts(self):
        checked = 0
        for size in range(1, 9):
            for values in combinations_with_replacement((-10000, -1, 0, 1, 10000), size):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 1286)

    def test_maximum_length_and_value_boundaries(self):
        self.check([0] * 30000)
        self.check([value for value in range(-7500, 7500) for _ in range(2)])
        self.check([-10000] * 15000 + [10000] * 15000)
        self.check([0, 0, 1, 1, 1, 1, 2, 3, 3])
        self.check([1, 1, 1, 2, 2, 3])
        self.check([10000])


if __name__ == '__main__':
    unittest.main()
