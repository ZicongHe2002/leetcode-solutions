import unittest
from itertools import combinations_with_replacement

from python.p0081_search_rotated_sorted_array_ii import Solution


class RotatedSearchTests(unittest.TestCase):
    def check(self, values, target):
        before = values[:]
        expected = target in before
        result = Solution().search(values, target)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_sorted_arrays_and_rotations(self):
        for size in range(1, 9):
            for values in combinations_with_replacement((-1, 0, 1, 3), size):
                for pivot in range(size):
                    rotated = list(values[pivot:] + values[:pivot])
                    for target in (-10000, -1, 0, 1, 2, 3, 10000):
                        self.check(rotated, target)

    def test_duplicate_boundaries_maximum_length_and_empty_extension(self):
        self.check([], 0)
        self.check([1, 0, 1, 1, 1], 0)
        self.check([3, 1, 1, 1], 3)
        self.check([1] * 5000, 0)
        self.check([1] * 5000, 1)
        base = [1] * 4999 + [2]
        for pivot in (0, 1, 2499, 4999):
            rotated = base[pivot:] + base[:pivot]
            for target in (0, 1, 2):
                self.check(rotated, target)
        base = list(range(-2500, 2500))
        rotated = base[2345:] + base[:2345]
        for target in (-2500, 0, 2499, 5000):
            self.check(rotated, target)
        self.check([10000, -10000], -10000)
        self.check([10000, -10000], 0)


if __name__ == '__main__':
    unittest.main()
