import unittest
from itertools import combinations, product

from python.p0435_non_overlapping_intervals import Solution


def minimum_removal_by_subsets(intervals):
    largest = 0
    for mask in range(1 << len(intervals)):
        selected = [intervals[i] for i in range(len(intervals)) if mask >> i & 1]
        compatible = all(max(a[0], b[0]) >= min(a[1], b[1]) for a, b in combinations(selected, 2))
        if compatible:
            largest = max(largest, len(selected))
    return len(intervals) - largest


class IntervalRemovalTests(unittest.TestCase):
    def check(self, intervals, expected=None):
        before = [interval[:] for interval in intervals]
        if expected is None:
            expected = minimum_removal_by_subsets(intervals)
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(intervals, before)

    def test_all_small_interval_sequences_against_subsets(self):
        possible = list(combinations((-1, 0, 1, 2), 2))
        checks = 0
        for size in range(1, 5):
            for intervals in product(possible, repeat=size):
                self.check([list(interval) for interval in intervals])
                checks += 1
        self.assertEqual(checks, 1554)

    def test_maximum_lengths_touching_duplicates_nested_and_empty_extension(self):
        self.check([[value, value + 1] for value in range(49999, -50001, -1)], 0)
        self.check([[-50000, 50000] for _ in range(100000)], 99999)
        self.check([[-5, 5], [-4, 4], [-3, 3], [-2, 2]], 3)
        self.check([[-50000, -1], [-1, 0], [0, 50000]], 0)
        self.check([[1, 2], [2, 3], [1, 3]], 1)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
