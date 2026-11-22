import unittest
from itertools import product

from python.p0162_find_peak_element import Solution


def peaks(values):
    return [index for index, value in enumerate(values)
            if (index == 0 or value > values[index - 1])
            and (index + 1 == len(values) or value > values[index + 1])]


class PeakTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        expected = peaks(values)
        self.assertTrue(expected)
        actual = Solution().findPeakElement(values)
        self.assertIs(type(actual), int)
        self.assertIn(actual, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_with_distinct_neighbors(self):
        checked = 0
        for size in range(1, 8):
            for values in product(range(-2, 3), repeat=size):
                if any(values[index] == values[index + 1] for index in range(size - 1)):
                    continue
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 27305)

    def test_multiple_peaks_length_and_integer_endpoints(self):
        for values in [[1, 2, 1, 3, 2], list(range(1000)), list(range(1000, 0, -1)),
                        [0, 1] * 500, [-2147483648], [-2147483648, 2147483647, -2147483648]]:
            self.check(values)


if __name__ == '__main__':
    unittest.main()
