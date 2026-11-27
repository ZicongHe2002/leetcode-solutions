import random
import unittest
from itertools import product

from python.p0766_toeplitz_matrix import Solution


def complete_diagonal_groups(matrix):
    groups = {}
    for row, values in enumerate(matrix):
        for column, value in enumerate(values):
            groups.setdefault(column - row, set()).add(value)
    return all(len(values) == 1 for values in groups.values())


class ToeplitzTests(unittest.TestCase):
    def check(self, matrix, expected=None):
        before = [row[:] for row in matrix]
        result = Solution().isToeplitzMatrix(matrix)
        self.assertIs(type(result), bool)
        self.assertEqual(result, complete_diagonal_groups(matrix) if expected is None else expected)
        self.assertEqual(matrix, before)

    def test_every_small_binary_matrix_against_complete_diagonal_sets(self):
        checked = 0
        for rows, columns in product(range(1, 4), repeat=2):
            for flat in product((0,1), repeat=rows * columns):
                matrix = [list(flat[start:start + columns]) for start in range(0, len(flat), columns)]
                self.check(matrix)
                checked += 1
        self.assertEqual(checked, 682)

    def test_seeded_maximum_diagonal_matrices_single_mutations_and_official_examples(self):
        rng = random.Random(766)
        for _ in range(100):
            values = {key: rng.randrange(100) for key in range(-19, 20)}
            matrix = [[values[column - row] for column in range(20)] for row in range(20)]
            self.check(matrix, True)
            matrix[10][10] = (matrix[10][10] + 1) % 100
            self.check(matrix, False)
        self.check([[1,2,3,4],[5,1,2,3],[9,5,1,2]], True)
        self.check([[1,2],[2,2]], False)
        self.check([[0,99] * 10], True)
        self.check([[value] for value in [0,99] * 10], True)
        self.check([[99]], True)


if __name__ == '__main__':
    unittest.main()
