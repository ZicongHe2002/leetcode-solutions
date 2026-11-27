from collections import Counter
from itertools import combinations
import unittest

from python.p0540_single_element_in_a_sorted_array import Solution


def frequency_oracle(values):
    return next(value for value, frequency in Counter(values).items() if frequency == 1)


class EvenPairBoundarySearchTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        actual = Solution().singleNonDuplicate(values)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, frequency_oracle(values) if expected is None else expected)
        self.assertEqual(values, before)

    def test_every_small_value_subset_and_single_choice_against_frequencies(self):
        count = 0
        for size in range(1, 9):
            for distinct in combinations(range(8), size):
                for single in distinct:
                    values = [value for value in distinct for _ in range(1 if value == single else 2)]
                    self.check(values)
                    count += 1
        self.assertEqual(count, 1024)

    def test_largest_legal_length_single_at_each_region_and_value_limits(self):
        for single in (0, 25000, 49999):
            values = [value for value in range(50000) for _ in range(1 if value == single else 2)]
            self.assertEqual(len(values), 99999)
            self.check(values, single)
        self.check([0], 0)
        self.check([100000], 100000)
        self.check([0, 0, 100000], 100000)
        self.check([0, 100000, 100000], 0)
        self.check([1, 1, 2, 3, 3, 4, 4, 8, 8], 2)
        self.check([3, 3, 7, 7, 10, 11, 11], 10)


if __name__ == '__main__':
    unittest.main()
