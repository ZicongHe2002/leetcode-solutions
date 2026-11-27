import random
import unittest
from itertools import product

from python.p0630_course_schedule_iii import Solution


def all_subset_orders(courses):
    count = len(courses)
    feasible = [False] * (1 << count)
    totals = [0] * (1 << count)
    feasible[0] = True
    best = 0
    for mask in range(1, 1 << count):
        bit = mask & -mask
        index = bit.bit_length() - 1
        totals[mask] = totals[mask ^ bit] + courses[index][0]
        for last in range(count):
            if mask & (1 << last):
                previous = mask ^ (1 << last)
                if feasible[previous] and totals[mask] <= courses[last][1]:
                    feasible[mask] = True
                    best = max(best, mask.bit_count())
                    break
    return best


class CourseScheduleTests(unittest.TestCase):
    def check(self, courses, expected=None):
        before = [row[:] for row in courses]
        if expected is None:
            expected = all_subset_orders(courses)
        actual = Solution().scheduleCourse(courses)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected, courses if len(courses) < 12 else None)
        self.assertEqual(courses, before)

    def test_small_sequences_and_seeded_samples_against_subset_orders(self):
        kinds = ((1, 1), (1, 2), (2, 2), (2, 3), (3, 2))
        checks = 0
        for size in range(7):
            for sequence in product(kinds, repeat=size):
                self.check([list(course) for course in sequence])
                checks += 1
        self.assertEqual(checks, 19531)
        rng = random.Random(630)
        for _ in range(200):
            size = rng.randint(7, 10)
            self.check([[rng.randint(1, 12), rng.randint(1, 30)]
                        for _ in range(size)])

    def test_maximum_lengths_deadline_equality_and_replacement(self):
        self.check([[1, 10000] for _ in range(10000)], 10000)
        self.check([[10000, 10000] for _ in range(10000)], 1)
        self.check([[10000, 9999] for _ in range(10000)], 0)
        self.check([[1, 1], [1, 2]], 2)
        self.check([[5, 5], [4, 6], [2, 6]], 2)
        self.check([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3)
        self.check([[3, 2], [4, 3]], 0)


if __name__ == '__main__':
    unittest.main()
