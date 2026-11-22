from itertools import product
import unittest

from python.p0413_arithmetic_slices import Solution


def direct_contiguous_intervals(values):
    return sum(all(values[index] - values[index - 1] == values[start + 1] - values[start]
                   for index in range(start + 2, end))
               for start in range(len(values))
               for end in range(start + 3, len(values) + 1))


class ContiguousArithmeticSliceTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = direct_contiguous_intervals(values)
        result = Solution().numberOfArithmeticSlices(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_direct_contiguous_interval_scans(self):
        checks = 0
        for size in range(1, 9):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_runs_breaks_and_allowed_value_endpoints(self):
        self.check([0] * 5000, 4999 * 4998 // 2)
        self.check([-1000] * 2500 + [1000] * 2500, 2 * (2499 * 2498 // 2))
        self.check([-1000, 1000] * 2500, 0)
        self.check(list(range(-1000, 1001)), 2000 * 1999 // 2)
        self.check([1, 2, 3, 4], 3)


if __name__ == '__main__':
    unittest.main()
