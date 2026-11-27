import unittest
from itertools import product

from python.p0697_degree_of_an_array import Solution


def degree(values):
    return max(values.count(value) for value in set(values))


def all_same_degree_intervals(values):
    desired = degree(values)
    for length in range(1, len(values) + 1):
        for start in range(len(values) - length + 1):
            if degree(values[start:start + length]) == desired:
                return length


class ArrayDegreeTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        result = Solution().findShortestSubArray(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, all_same_degree_intervals(values) if expected is None else expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_every_contiguous_interval_degree(self):
        checked = 0
        for size in range(1, 8):
            for values in product((0, 1, 2), repeat=size):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 3279)

    def test_fifty_thousand_elements_tied_degrees_and_extreme_legal_values(self):
        self.check(list(range(50000)), 1)
        self.check([49999] * 50000, 50000)
        self.check([0] * 25000 + [49999] * 25000, 25000)
        self.check([0, 49999] * 25000, 49999)
        self.check([0] * 20000 + [1] * 20000 + [0] * 10000, 50000)
        self.check([1, 2, 2, 3, 1], 2)
        self.check([1, 2, 2, 3, 1, 4, 2], 6)


if __name__ == '__main__':
    unittest.main()
