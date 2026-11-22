from itertools import product
import unittest

from python.p0274_h_index import Solution


def definition(values):
    return max(h for h in range(len(values) + 1) if sum(value >= h for value in values) >= h)


class CitationBucketTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = definition(values)
        result = Solution().hIndex(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_unsorted_citations_against_direct_definition(self):
        checks = 0
        for size in range(1, 8):
            for values in product((0, 1, 3, 5), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 21844)

    def test_maximum_papers_citation_limit_and_zero_threshold(self):
        self.check([1000] * 5000, 1000)
        self.check([0] * 5000, 0)
        self.check([1] * 5000, 1)
        self.check([0] * 4000 + [1000] * 1000, 1000)
        self.check([3, 0, 6, 1, 5])


if __name__ == '__main__':
    unittest.main()
