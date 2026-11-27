from itertools import combinations_with_replacement
import unittest

from python.p0495_teemo_attacking import Solution


def poisoned_second_set(times, duration):
    return len({second for time in times for second in range(time, time + duration)})


class PoisonIntervalUnionTests(unittest.TestCase):
    def check(self, times, duration, expected=None):
        before = times[:]
        actual = Solution().findPoisonedDuration(times, duration)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, poisoned_second_set(times, duration) if expected is None else expected)
        self.assertEqual(times, before)

    def test_all_small_nondecreasing_times_and_durations_against_second_sets(self):
        arrays = queries = 0
        for size in range(7):
            for times in combinations_with_replacement(range(6), size):
                arrays += 1
                for duration in range(6):
                    self.check(list(times), duration)
                    queries += 1
        self.assertEqual((arrays, queries), (924, 5544))

    def test_maximum_attack_count_time_duration_duplicates_and_touching(self):
        times = [1000 * index for index in range(10000)]
        self.check(times, 10000000, times[-1] + 10000000)
        self.check([10000000] * 10000, 10000000, 10000000)
        self.check(list(range(10000)), 0, 0)
        self.check([1, 3], 2, 4)
        self.check([1, 2], 2, 3)
        self.check([2, 2], 3, 3)
        self.check([0, 10000000], 1, 2)


if __name__ == '__main__':
    unittest.main()
