from itertools import combinations, product
import unittest

from python.p0548_split_array_with_equal_sum import Solution


def literal_three_cuts_oracle(values):
    for first, middle, last in combinations(range(1, len(values) - 1), 3):
        if middle <= first + 1 or last <= middle + 1:
            continue
        pieces = (values[:first], values[first + 1:middle], values[middle + 1:last], values[last + 1:])
        if len(set(map(sum, pieces))) == 1:
            return True
    return False


class FourExcludedCutSumTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        actual = Solution().splitArray(values)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, literal_three_cuts_oracle(values) if expected is None else expected)
        self.assertEqual(values, before)

    def test_every_short_signed_array_against_all_legal_cut_triples(self):
        arrays = 0
        for size in range(1, 10):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                arrays += 1
        self.assertEqual(arrays, 29523)

    def test_maximum_length_numeric_limits_and_excluded_cut_values(self):
        self.check([0] * 2000, True)
        self.check([1] * 2000, False)
        self.check([1] * 1999, True)
        self.check([-10**6] * 2000, False)
        self.check([-10**6] * 1999, True)
        values = [0] * 2000
        values[1], values[3], values[5] = 10**6, -10**6, 10**6
        self.check(values, True)
        self.check([1, 2, 1, 2, 1, 2, 1], True)
        self.check([1, 2, 1, 2, 1, 2, 1, 2], False)


if __name__ == '__main__':
    unittest.main()
