import unittest
from itertools import combinations

from python.p0057_insert_interval import Solution


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


class InsertIntervalTests(unittest.TestCase):
    def check(self, intervals, new_interval, expected):
        before, rows = [row[:] for row in intervals], intervals[:]
        new_before = new_interval[:]
        result = Solution().insert(intervals, new_interval)
        self.assertEqual(result, expected)
        self.assertEqual(intervals, before)
        self.assertEqual(new_interval, new_before)
        self.assertEqual(len({id(row) for row in result}), len(result))
        self.assertFalse({id(row) for row in result} & ({id(row) for row in intervals} | {id(new_interval)}))
        for actual, original in zip(intervals, rows):
            self.assertIs(actual, original)

    def test_all_small_sorted_disjoint_lists_and_insertions_against_components(self):
        possible = [(start, end) for start in range(5) for end in range(start, 5)]
        arrays = checks = 0
        for size in range(6):
            for values in combinations(possible, size):
                if any(a[1] >= b[0] for a, b in zip(values, values[1:])):
                    continue
                arrays += 1
                for new in possible:
                    intervals = [list(pair) for pair in values]
                    self.check(intervals, list(new), component_oracle(intervals + [list(new)]))
                    checks += 1
        self.assertEqual((arrays, checks), (89, 1335))

    def test_examples_aliasing_and_maximum_contract(self):
        self.check([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])
        self.check([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]])
        self.check([], [0, 100000], [[0, 100000]])
        points = [[2 * index, 2 * index] for index in range(10000)]
        self.check(points, [0, 100000], [[0, 100000]])
        self.check(points, [100000, 100000], [row[:] for row in points] + [[100000, 100000]])


if __name__ == '__main__':
    unittest.main()
