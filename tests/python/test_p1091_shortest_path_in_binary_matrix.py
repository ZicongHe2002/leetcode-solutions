import unittest
from itertools import product

from python.p1091_shortest_path_in_binary_matrix import Solution


def floyd_grid_cells(grid):
    size = len(grid)
    if grid[0][0] or grid[-1][-1]:
        return -1
    count, infinity = size * size, 999
    distance = [[infinity] * count for _ in range(count)]
    cells = [(row, column) for row in range(size) for column in range(size) if not grid[row][column]]
    for row, column in cells:
        first = row * size + column
        distance[first][first] = 0
        for nr, nc in cells:
            if max(abs(row - nr), abs(column - nc)) == 1:
                distance[first][nr * size + nc] = 1
    for middle in range(count):
        for first in range(count):
            for second in range(count):
                distance[first][second] = min(distance[first][second], distance[first][middle] + distance[middle][second])
    return -1 if distance[0][-1] == infinity else distance[0][-1] + 1


class BinaryMatrixPathTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before = [row[:] for row in grid]
        if expected is None:
            expected = floyd_grid_cells(grid)
        result = Solution().shortestPathBinaryMatrix(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(grid, before)

    def test_all_small_square_patterns_against_floyd_graph(self):
        checks = 0
        for size in range(1, 4):
            for values in product((0, 1), repeat=size * size):
                self.check([list(values[row * size:(row + 1) * size]) for row in range(size)])
                checks += 1
        self.assertEqual(checks, 530)

    def test_maximum_grid_diagonal_barrier_and_corner_cut(self):
        self.check([[0] * 100 for _ in range(100)], 100)
        grid = [[0] * 100 for _ in range(100)]
        grid[50] = [1] * 100
        self.check(grid, -1)
        self.check([[int(row != column) for column in range(100)] for row in range(100)], 100)
        self.check([[0 if row == 0 or column == 99 else 1 for column in range(100)] for row in range(100)], 198)
        self.check([[0, 1], [1, 0]], 2)
        self.check([[1]], -1)


if __name__ == '__main__':
    unittest.main()
