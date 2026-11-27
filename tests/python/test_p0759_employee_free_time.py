import unittest
from itertools import combinations, product

import python.p0759_employee_free_time as solution_module


class Interval:
    def __init__(self, start, end):
        self.start, self.end = start, end


solution_module.Interval = Interval


def uncovered_unit_midpoints(schedule):
    left = min(start for row in schedule for start, _ in row)
    right = max(end for row in schedule for _, end in row)
    result, begin = [], None
    for point in range(left, right):
        free = not any(2 * start < 2 * point + 1 < 2 * end for row in schedule for start, end in row)
        if free and begin is None:
            begin = point
        elif not free and begin is not None:
            result.append((begin, point))
            begin = None
    if begin is not None:
        result.append((begin, right))
    return result


class EmployeeFreeTimeTests(unittest.TestCase):
    def check(self, schedule, expected=None):
        objects = [[Interval(start, end) for start, end in row] for row in schedule]
        before = [[(id(interval), interval.start, interval.end) for interval in row] for row in objects]
        row_ids = list(map(id, objects))
        result = solution_module.Solution().employeeFreeTime(objects)
        self.assertIs(type(result), list)
        self.assertTrue(all(isinstance(interval, Interval) for interval in result))
        actual = [(interval.start, interval.end) for interval in result]
        self.assertEqual(actual, uncovered_unit_midpoints(schedule) if expected is None else expected, schedule)
        self.assertTrue(all(start < end for start, end in actual))
        self.assertTrue(all(a[1] < b[0] for a, b in zip(actual, actual[1:])))
        self.assertTrue(all(id(interval) not in {item[0] for row in before for item in row} for interval in result))
        self.assertEqual([[(id(interval), interval.start, interval.end) for interval in row] for row in objects], before)
        self.assertEqual(list(map(id, objects)), row_ids)

    def test_all_small_legal_schedules_against_individual_unit_midpoint_coverage(self):
        intervals = list(combinations(range(5), 2))
        options = []
        for mask in range(1, 1 << len(intervals)):
            row = sorted(intervals[index] for index in range(len(intervals)) if mask >> index & 1)
            if all(a[1] <= b[0] for a, b in zip(row, row[1:])):
                options.append(row)
        self.assertEqual(len(options), 33)
        checked = 0
        for employees in range(1, 4):
            for schedule in product(options, repeat=employees):
                self.check(schedule)
                checked += 1
        self.assertEqual(checked, 37059)

    def test_official_examples_touching_nested_and_maximum_schedule_shape(self):
        self.check([[(1,2),(5,6)],[(1,3)],[(4,10)]], [(3,4)])
        self.check([[(1,3),(6,7)],[(2,4)],[(2,5),(9,12)]], [(5,6),(7,9)])
        self.check([[(0,10**8)],[(1,2),(3,4)]], [])
        self.check([[(0,1)],[(1,2)]], [])
        self.check([[(0,1),(10**8 - 1,10**8)]], [(1,10**8 - 1)])
        row = [(2 * index, 2 * index + 1) for index in range(50)]
        self.check([row[:] for _ in range(50)], [(2 * index + 1, 2 * index + 2) for index in range(49)])


if __name__ == '__main__':
    unittest.main()
