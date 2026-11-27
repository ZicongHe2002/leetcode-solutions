from itertools import combinations_with_replacement
import unittest

from python.p0275_h_index_ii import Solution


def definition(values):
    return max(h for h in range(len(values) + 1) if sum(value >= h for value in values) >= h)


class SortedCitationBoundaryTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = definition(values)
        result = Solution().hIndex(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_sorted_citations_against_direct_definition(self):
        checks = 0
        for size in range(1, 9):
            for values in combinations_with_replacement((0, 1, 3, 8), size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 494)

    def test_maximum_length_sentinel_and_citation_limit(self):
        self.check([1000] * 100000, 1000)
        self.check([0] * 100000, 0)
        self.check([1] * 100000, 1)
        self.check([0] * 99000 + [1000] * 1000, 1000)
        self.check([0, 1, 3, 5, 6])
        self.check(list(range(1000)))


if __name__ == '__main__':
    unittest.main()
