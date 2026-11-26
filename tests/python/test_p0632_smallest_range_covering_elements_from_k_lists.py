import random
import unittest
from itertools import combinations_with_replacement, product

from python.p0632_smallest_range_covering_elements_from_k_lists import Solution


def all_row_choices(rows):
    candidates = ((max(chosen) - min(chosen), min(chosen), max(chosen))
                  for chosen in product(*rows))
    _, left, right = min(candidates)
    return [left, right]


class SmallestCoveringRangeTests(unittest.TestCase):
    def check(self, rows, expected=None):
        before = [values[:] for values in rows]
        if expected is None:
            expected = all_row_choices(rows)
        actual = Solution().smallestRange(rows)
        self.assertIs(type(actual), list)
        self.assertEqual(actual, expected)
        self.assertEqual(rows, before)

    def test_small_sorted_rows_and_samples_against_cartesian_product(self):
        kinds = [values for size in range(1, 4)
                 for values in combinations_with_replacement((-2, 0, 3), size)]
        checks = 0
        for count in range(1, 4):
            for rows in product(kinds, repeat=count):
                self.check([list(values) for values in rows])
                checks += 1
        self.assertEqual((len(kinds), checks), (19, 7239))
        rng = random.Random(632)
        for _ in range(200):
            self.check([sorted(rng.randint(-20, 20) for _ in range(rng.randint(1, 5)))
                        for _ in range(rng.randint(1, 6))])

    def test_maximum_counts_ties_zero_width_and_extreme_endpoints(self):
        rows = [[-100000 + row + 3500 * offset for offset in range(50)]
                for row in range(3500)]
        self.check(rows, [-100000, -96501])
        self.check([[-100000], [100000]], [-100000, 100000])
        self.check([[-100000 + index for index in range(50)]], [-100000, -100000])
        self.check([[1, 5], [2, 6]], [1, 2])
        self.check([[1, 2, 3]] * 3, [1, 1])
        self.check([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24])


if __name__ == '__main__':
    unittest.main()
