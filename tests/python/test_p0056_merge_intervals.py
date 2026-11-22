import unittest
from itertools import product

from python.p0056_merge_intervals import Solution


def component_oracle(intervals):
    parent = list(range(len(intervals)))

    def find(index):
        while parent[index] != index:
            index = parent[index]
        return index

    for a in range(len(intervals)):
        for b in range(a):
            if max(intervals[a][0], intervals[b][0]) <= min(intervals[a][1], intervals[b][1]):
                parent[find(a)] = find(b)
    groups = {}
    for index, (start, end) in enumerate(intervals):
        groups.setdefault(find(index), []).append((start, end))
    return sorted([[min(start for start, end in group), max(end for start, end in group)]
                   for group in groups.values()])


class MergeIntervalTests(unittest.TestCase):
    def check(self, intervals, expected):
        before, rows = [row[:] for row in intervals], intervals[:]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected)
        self.assertEqual(intervals, before)
        self.assertEqual(len({id(row) for row in result}), len(result))
        self.assertFalse({id(row) for row in result} & {id(row) for row in intervals})
        for actual, original in zip(intervals, rows):
            self.assertIs(actual, original)

    def test_all_small_ordered_interval_lists_against_graph_components(self):
        possible = [(start, end) for start in range(4) for end in range(start, 4)]
        checks = 0
        for size in range(5):
            for values in product(possible, repeat=size):
                intervals = [list(pair) for pair in values]
                self.check(intervals, component_oracle(intervals))
                checks += 1
        self.assertEqual(checks, 11111)

    def test_examples_touching_points_and_maximum_interval_count(self):
        self.check([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])
        self.check([[1, 4], [4, 5]], [[1, 5]])
        self.check([[0, 0], [1, 1]], [[0, 0], [1, 1]])
        self.check([[1, 10], [2, 3], [3, 8]], [[1, 10]])
        self.check([[index, index + 1] for index in range(10000)], [[0, 10000]])
        points = [[index, index] for index in range(10000)]
        self.check(points, [[index, index] for index in range(10000)])
        self.check([], [])


if __name__ == '__main__':
    unittest.main()
