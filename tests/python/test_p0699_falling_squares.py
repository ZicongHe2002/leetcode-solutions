import random
import unittest
from itertools import product

from python.p0699_falling_squares import Solution


def unit_column_heights(positions):
    columns, answer = {}, []
    for left, side in positions:
        top = max((columns.get(x, 0) for x in range(left, left + side)), default=0) + side
        for x in range(left, left + side):
            columns[x] = top
        answer.append(max(columns.values()))
    return answer


class FallingSquaresTests(unittest.TestCase):
    def check(self, positions, expected=None):
        before = [position[:] for position in positions]
        row_ids = [id(position) for position in positions]
        result = Solution().fallingSquares(positions)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result, unit_column_heights(positions) if expected is None else expected)
        self.assertEqual(positions, before)
        self.assertEqual([id(position) for position in positions], row_ids)

    def test_all_short_drop_sequences_against_actual_unit_columns(self):
        choices = tuple(product(range(1, 5), range(1, 4)))
        checked = 0
        for size in range(1, 5):
            for sequence in product(choices, repeat=size):
                self.check([list(position) for position in sequence])
                checked += 1
        self.assertEqual(checked, 22620)
        rng = random.Random(699)
        for _ in range(200):
            self.check([[rng.randrange(1, 21), rng.randrange(1, 11)]
                        for _ in range(rng.randrange(1, 21))])

    def test_thousand_squares_large_coordinates_heights_touching_and_overlap(self):
        self.check([[10**8, 10**6] for _ in range(1000)], [10**6 * i for i in range(1, 1001)])
        self.check([[1 + 1000 * i, 1000] for i in range(1000)], [1000] * 1000)
        self.check([[10**8, 10**6], [10**8 - 1, 1], [10**8 - 1, 2]], [10**6, 10**6, 10**6 + 2])
        self.check([[100, 100], [200, 100]], [100, 100])
        self.check([[1, 2], [2, 3], [6, 1]], [2, 5, 5])


if __name__ == '__main__':
    unittest.main()
