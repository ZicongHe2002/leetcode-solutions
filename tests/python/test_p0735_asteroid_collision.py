import unittest
from itertools import product

from python.p0735_asteroid_collision import Solution


def adjacent_collision_reductions(values):
    current = values[:]
    while True:
        for index in range(len(current) - 1):
            left, right = current[index:index + 2]
            if left > 0 and right < 0:
                replacement = [left] if left > -right else [right] if left < -right else []
                current[index:index + 2] = replacement
                break
        else:
            return current


class AsteroidCollisionTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = adjacent_collision_reductions(values)
        result = Solution().asteroidCollision(values)
        self.assertIs(type(result), list)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_nonzero_arrays_against_adjacent_reductions(self):
        checks = 0
        for size in range(8):
            for values in product((-2, -1, 1, 2), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 21845)

    def test_maximum_length_size_equal_collisions_and_separating_directions(self):
        self.check([1] * 9999 + [-1000], [-1000])
        self.check([-1000] * 5000 + [1000] * 5000, [-1000] * 5000 + [1000] * 5000)
        self.check([1000, -1000] * 5000, [])
        self.check([1000] * 5000 + [-1] * 5000, [1000] * 5000)
        self.check([10, 2, -5], [10])


if __name__ == '__main__':
    unittest.main()
