import unittest
from itertools import combinations

from python.p1552_magnetic_force_between_two_balls import Solution


def all_ball_placements(positions, count):
    return max(min(abs(left - right) for left, right in combinations(chosen, 2))
               for chosen in combinations(positions, count))


class MagneticDistanceTests(unittest.TestCase):
    def check(self, positions, count, expected=None):
        before = positions[:]
        if expected is None:
            expected = all_ball_placements(positions, count)
        result = Solution().maxDistance(positions, count)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(positions, before)

    def test_small_coordinate_subsets_against_all_ball_placements(self):
        arrays = checks = 0
        for size in range(2, 8):
            for positions in combinations(range(1, 10), size):
                arrays += 1
                for count in range(2, size + 1):
                    self.check(list(reversed(positions)), count)
                    checks += 1
        self.assertEqual((arrays, checks), (492, 1722))

    def test_maximum_length_span_and_number_of_balls(self):
        positions = list(range(100000, 0, -1))
        self.check(positions, 100000, 1)
        self.check(positions, 2, 99999)
        self.check(positions, 50000, 2)
        self.check([10**9, 1], 2, 999999999)
        self.check([1, 2, 3, 4, 7], 3, 3)


if __name__ == '__main__':
    unittest.main()
