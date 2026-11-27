from itertools import product
import unittest

from python.p0165_compare_version_numbers import Solution


class VersionNumericTupleOracleTests(unittest.TestCase):
    def check(self, first, second, expected):
        result = Solution().compareVersion(first, second)
        self.assertIs(type(result), int)
        self.assertIn(result, (-1, 0, 1))
        self.assertEqual(result, expected)

    def test_every_small_version_pair_with_generated_numeric_meaning(self):
        segments = (('0', 0), ('00', 0), ('1', 1), ('01', 1), ('2', 2), ('002', 2))
        versions = []
        for length in range(1, 4):
            for pieces in product(segments, repeat=length):
                versions.append(('.'.join(piece[0] for piece in pieces), tuple(piece[1] for piece in pieces)))
        checks = 0
        for first, left in versions:
            for second, right in versions:
                width = max(len(left), len(right))
                padded_left = left + (0,) * (width - len(left))
                padded_right = right + (0,) * (width - len(right))
                self.check(first, second, (padded_left > padded_right) - (padded_left < padded_right))
                checks += 1
        self.assertEqual((len(versions), checks), (258, 66564))

    def test_maximum_lengths_many_zero_revisions_and_int32_values(self):
        longest = '0' * 490 + '2147483647'
        self.assertEqual(len(longest), 500)
        self.check(longest, '2147483647', 0)
        self.check('0' * 500, '0', 0)
        self.check('1' + '.0' * 249, '1', 0)
        self.check('2147483647.0', '2147483646.999', 1)
        self.check('1.2', '1.10', -1)
        self.check('1.01', '1.001', 0)


if __name__ == '__main__':
    unittest.main()
