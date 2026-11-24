import unittest
from itertools import product

from python.p0904_fruit_into_baskets import Solution


def all_intervals(values):
    return max((end - start for start in range(len(values))
                for end in range(start + 1, len(values) + 1)
                if len(set(values[start:end])) <= 2), default=0)


class FruitWindowTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = all_intervals(values)
        result = Solution().totalFruit(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_legal_type_arrays_against_slice_sets(self):
        checks = 0
        for size in range(9):
            for values in product(range(min(3, size)), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 9834)

    def test_maximum_lengths_and_third_type_at_end(self):
        self.check([0] * 100000, 100000)
        self.check([0, 1] * 50000, 100000)
        self.check([0, 1, 2] * 33333 + [0], 2)
        self.check([0] * 99998 + [1, 2], 99999)
        self.check([1, 2, 1], 3)


if __name__ == '__main__':
    unittest.main()
