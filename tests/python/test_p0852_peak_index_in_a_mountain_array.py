import unittest
from itertools import combinations

from python.p0852_peak_index_in_a_mountain_array import Solution


def all_small_mountains():
    for peak in range(1, 6):
        slopes = [values for size in range(1, peak + 1)
                  for values in combinations(range(peak), size)]
        for left in slopes:
            for right in slopes:
                yield list(left) + [peak] + list(reversed(right))


class MountainPeakTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        expected = values.index(max(values))
        self.assertTrue(0 < expected < len(values) - 1)
        self.assertTrue(all(values[i] < values[i + 1] for i in range(expected)))
        self.assertTrue(all(values[i] > values[i + 1]
                            for i in range(expected, len(values) - 1)))
        actual = Solution().peakIndexInMountainArray(values)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected)
        self.assertEqual(values, before)

    def test_all_small_strict_mountains_against_linear_peak(self):
        checks = 0
        for values in all_small_mountains():
            self.check(values)
            checks += 1
        self.assertEqual(checks, 1245)

    def test_maximum_length_and_peaks_near_both_ends(self):
        mountains = [
            list(range(50000)) + [10**6] + list(range(49998, -1, -1)),
            [0, 10**6] + list(range(99997, -1, -1)),
            list(range(99999)) + [0],
        ]
        for values in mountains:
            self.assertEqual(len(values), 100000)
            self.check(values)
        self.check([0, 1, 0])
        self.check([0, 10, 5, 2])


if __name__ == '__main__':
    unittest.main()
