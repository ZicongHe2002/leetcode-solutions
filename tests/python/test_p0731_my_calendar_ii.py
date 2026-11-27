import unittest
from itertools import product

from python.p0731_my_calendar_ii import MyCalendarTwo


class CalendarTwoTests(unittest.TestCase):
    def check(self, requests, known=None):
        obj, deltas, actual = MyCalendarTwo(), {}, []
        for start, end in requests:
            trial = dict(deltas)
            trial[start] = trial.get(start, 0) + 1
            trial[end] = trial.get(end, 0) - 1
            depth = maximum = 0
            for point in sorted(trial):
                depth += trial[point]
                maximum = max(maximum, depth)
            expected = maximum <= 2
            if expected:
                deltas = trial
            result = obj.book(start, end)
            self.assertIs(type(result), bool)
            self.assertEqual(result, expected, requests[:10])
            actual.append(result)
        if known is not None:
            self.assertEqual(actual, known)

    def test_all_short_booking_programs_against_complete_endpoint_sweep(self):
        intervals = [(start, end) for start in range(4) for end in range(start + 1, 5)]
        programs = calls = 0
        for length in range(1, 5):
            for requests in product(intervals, repeat=length):
                self.check(requests)
                programs += 1
                calls += length
        self.assertEqual((programs, calls), (11110, 43210))

    def test_examples_thousand_call_boundaries_and_failed_booking_preservation(self):
        self.check([(10,20),(50,60),(10,40),(5,15),(5,10),(25,55)],
                   [True,True,True,False,True,True])
        self.check([(0,10),(0,10),(0,10),(10,20),(10,20),(10,20)],
                   [True,True,False,True,True,False])
        self.check([(i, i + 1) for i in range(10**9 - 500, 10**9) for _ in range(2)], [True] * 1000)
        self.check([(0,10**9)] * 2 + [(i,i + 1) for i in range(998)], [True] * 2 + [False] * 998)


if __name__ == '__main__':
    unittest.main()
