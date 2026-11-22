import unittest
from itertools import combinations, product

from python.p1482_minimum_number_of_days_to_make_m_bouquets import Solution


def explicit_disjoint_bouquets(values, bouquets, width):
    if bouquets * width > len(values):
        return -1
    for day in sorted(set(values)):
        for starts in combinations(range(len(values) - width + 1), bouquets):
            if any(starts[i + 1] - starts[i] < width for i in range(len(starts) - 1)):
                continue
            if all(all(bloom <= day for bloom in values[start:start + width]) for start in starts):
                return day
    return -1


class BouquetDayTests(unittest.TestCase):
    def check(self, values, bouquets, width, expected=None):
        before = values[:]
        if expected is None:
            expected = explicit_disjoint_bouquets(values, bouquets, width)
        result = Solution().minDays(values, bouquets, width)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_small_bloom_arrays_against_explicit_disjoint_intervals(self):
        arrays = checks = 0
        for size in range(1, 7):
            for values in product((1, 2, 3), repeat=size):
                arrays += 1
                for width in range(1, size + 1):
                    for bouquets in range(1, size // width + 2):
                        self.check(list(values), bouquets, width)
                        checks += 1
        self.assertEqual((arrays, checks), (1092, 19464))

    def test_maximum_lengths_dates_adjacency_and_impossible_counts(self):
        self.check([10**9] * 100000, 1, 100000, 10**9)
        self.check([1] * 100000, 100000, 1, 1)
        self.check([1] * 100000, 100001, 1, -1)
        self.check([1, 10**9] * 50000, 50000, 2, 10**9)
        self.check([1, 10**9] * 50000, 50001, 2, -1)
        self.check([1, 10, 3, 10, 2], 3, 1, 3)


if __name__ == '__main__':
    unittest.main()
