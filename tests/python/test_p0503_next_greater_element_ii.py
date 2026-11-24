import unittest
from itertools import product

from python.p0503_next_greater_element_ii import Solution


def explicit_circular_scans(values):
    return [next((values[(index + step) % len(values)] for step in range(1, len(values))
                  if values[(index + step) % len(values)] > value), -1)
            for index, value in enumerate(values)]


class CircularNextGreaterTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = explicit_circular_scans(values)
        result = Solution().nextGreaterElements(values)
        self.assertIs(type(result), list)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_against_explicit_circular_steps(self):
        checks = 0
        for size in range(8):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 3280)

    def test_maximum_length_duplicates_wrap_and_extreme_values(self):
        self.check([0] * 10000, [-1] * 10000)
        self.check(list(range(10000)), list(range(1, 10000)) + [-1])
        self.check(list(range(9999, -1, -1)), [-1] + [9999] * 9999)
        self.check([-10**9, 0, 10**9], [0, 10**9, -1])
        self.check([-2, -1], [-1, -1])
        self.check([1, 2, 1], [2, -1, 2])


if __name__ == '__main__':
    unittest.main()
