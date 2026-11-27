from itertools import combinations, product
import unittest

from python.p0539_minimum_time_difference import Solution


def clock_text(minute):
    return f'{minute // 60:02d}:{minute % 60:02d}'


def all_circular_pairs_oracle(times):
    minutes = [int(text.split(':')[0]) * 60 + int(text.split(':')[1]) for text in times]
    return min(min(abs(left - right), 1440 - abs(left - right))
               for left, right in combinations(minutes, 2))


class CircularMinuteGapTests(unittest.TestCase):
    def check(self, times, expected=None):
        before = times[:]
        actual = Solution().findMinDifference(times)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, all_circular_pairs_oracle(times) if expected is None else expected)
        self.assertEqual(times, before)

    def test_all_short_time_lists_against_every_circular_pair(self):
        vocabulary = tuple(map(clock_text, (0, 1, 59, 60, 720, 1439)))
        count = 0
        for size in range(2, 6):
            for times in product(vocabulary, repeat=size):
                self.check(list(times))
                count += 1
        self.assertEqual(count, 9324)

    def test_every_adjacent_minute_pair_full_day_and_maximum_input_count(self):
        for minute in range(1440):
            self.check([clock_text(minute), clock_text((minute + 1) % 1440)], 1)
        self.check([clock_text(minute) for minute in range(1439, -1, -1)], 1)
        self.check(['23:59'] * 20000, 0)
        self.check(['00:00', '12:00'], 720)
        self.check(['23:59', '00:00'], 1)
        self.check(['05:31', '22:08', '00:35'])


if __name__ == '__main__':
    unittest.main()
