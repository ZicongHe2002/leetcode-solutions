import unittest
from itertools import product

from python.p0729_my_calendar_i import MyCalendar


class CalendarOneTests(unittest.TestCase):
    def check_small(self, requests):
        obj, occupied = MyCalendar(), set()
        for start, end in requests:
            slots = set(range(start, end))
            expected = not bool(occupied & slots)
            if expected:
                occupied.update(slots)
            result = obj.book(start, end)
            self.assertIs(type(result), bool)
            self.assertEqual(result, expected, requests)

    def test_all_short_booking_programs_against_unit_time_occupancy(self):
        intervals = [(start, end) for start in range(4) for end in range(start + 1, 5)]
        programs = calls = 0
        for length in range(1, 5):
            for requests in product(intervals, repeat=length):
                self.check_small(requests)
                programs += 1
                calls += length
        self.assertEqual((programs, calls), (11110, 43210))

    def test_thousand_calls_extreme_endpoints_rejections_and_touching_events(self):
        obj = MyCalendar()
        for start in range(10**9 - 1000, 10**9):
            self.assertIs(obj.book(start, start + 1), True)
        obj = MyCalendar()
        self.assertIs(obj.book(0, 10**9), True)
        for start in range(999):
            self.assertIs(obj.book(start, start + 1), False)
        obj = MyCalendar()
        for request, expected in (((10,20), True), ((15,25), False), ((20,30), True),
                                  ((0,10), True), ((0,10), False), ((30,10**9), True)):
            self.assertIs(obj.book(*request), expected)


if __name__ == '__main__':
    unittest.main()
