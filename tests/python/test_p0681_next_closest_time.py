import unittest
from itertools import product

from python.p0681_next_closest_time import Solution


def digit_combinations(time):
    digits = set(time.replace(':', ''))
    start = int(time[:2]) * 60 + int(time[3:])
    candidates = []
    for first, second, third, fourth in product(digits, repeat=4):
        hour, minute = int(first + second), int(third + fourth)
        if hour < 24 and minute < 60:
            text = first + second + ':' + third + fourth
            delay = (hour * 60 + minute - start) % 1440 or 1440
            candidates.append((delay, text))
    return min(candidates)[1]


class NextClosestTimeTests(unittest.TestCase):
    def check(self, time, expected=None):
        result = Solution().nextClosestTime(time)
        self.assertIs(type(result), str)
        self.assertEqual(result, digit_combinations(time) if expected is None else expected)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[2], ':')
        self.assertTrue(0 <= int(result[:2]) < 24 and 0 <= int(result[3:]) < 60)

    def test_every_minute_against_allowed_digit_cartesian_product(self):
        for minute in range(1440):
            self.check(f'{minute // 60:02d}:{minute % 60:02d}')

    def test_midnight_leading_zero_and_full_day_wait(self):
        self.check('19:34', '19:39')
        self.check('23:59', '22:22')
        for time in ('00:00', '11:11', '22:22'):
            self.check(time, time)
        for time in ('00:01', '09:09', '10:00', '20:48', '23:58'):
            self.check(time)


if __name__ == '__main__':
    unittest.main()
