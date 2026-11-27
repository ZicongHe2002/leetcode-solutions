import unittest
from itertools import product

from python.p0732_my_calendar_iii import MyCalendarThree


class CalendarThreeTests(unittest.TestCase):
    def check(self, requests, known=None):
        obj, intervals, actual = MyCalendarThree(), [], []
        for start, end in requests:
            intervals.append((start, end))
            expected = max(sum(left <= point < right for left, right in intervals)
                           for point, _ in intervals)
            result = obj.book(start, end)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected, requests)
            actual.append(result)
        if known is not None:
            self.assertEqual(actual, known)

    def test_all_short_booking_programs_against_original_interval_coverage(self):
        intervals = [(start, end) for start in range(4) for end in range(start + 1, 5)]
        programs = calls = 0
        for length in range(1, 5):
            for requests in product(intervals, repeat=length):
                self.check(requests)
                programs += 1
                calls += length
        self.assertEqual((programs, calls), (11110, 43210))

    def test_official_history_and_four_hundred_call_extreme_families(self):
        self.check([(10,20),(50,60),(10,40),(5,15),(5,10),(25,55)], [1,1,2,3,3,3])
        for requests, expected in (
                ([(0,10**9)] * 400, list(range(1, 401))),
                ([(10**9 - 400 + i,10**9 - 399 + i) for i in range(400)], [1] * 400),
                ([(i,10**9 - i) for i in range(400)], list(range(1, 401)))):
            obj = MyCalendarThree()
            self.assertEqual([obj.book(*request) for request in requests], expected)


if __name__ == '__main__':
    unittest.main()
