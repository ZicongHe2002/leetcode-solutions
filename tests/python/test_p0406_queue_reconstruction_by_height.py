from collections import Counter
from itertools import product
import unittest

from python.p0406_queue_reconstruction_by_height import Solution


class HeightQueueConstraintTests(unittest.TestCase):
    def check(self, people):
        before = [person[:] for person in people]
        result = Solution().reconstructQueue(people)
        self.assertIs(type(result), list)
        self.assertEqual(Counter(map(tuple, result)), Counter(map(tuple, before)))
        for index, (height, count) in enumerate(result):
            self.assertEqual(sum(person[0] >= height for person in result[:index]), count)
        self.assertEqual(people, before)

    def test_every_small_height_queue_with_independently_derived_constraints(self):
        checks = 0
        for size in range(1, 7):
            for heights in product((0, 1, 2), repeat=size):
                people = [[height, sum(previous >= height for previous in heights[:index])]
                          for index, height in enumerate(heights)]
                self.check(list(reversed(people)))
                checks += 1
        self.assertEqual(checks, 1092)

    def test_maximum_people_same_heights_front_insertions_and_value_limit(self):
        self.check([[0, count] for count in range(1999, -1, -1)])
        self.check([[height, 0] for height in range(1, 2001)])
        self.check([[10**6, count] for count in range(1999, -1, -1)])


if __name__ == '__main__':
    unittest.main()
