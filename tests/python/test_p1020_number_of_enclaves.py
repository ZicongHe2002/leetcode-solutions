from itertools import product
import unittest

from python.p1020_number_of_enclaves import Solution


def each_land_cell_escape(grid):
    rows, columns = len(grid), len(grid[0])

    def escapes(start):
        pending, seen = [start], {start}
        while pending:
            row, column = pending.pop()
            if row in (0, rows - 1) or column in (0, columns - 1):
                return True
            for cell in ((row - 1, column), (row + 1, column),
                         (row, column - 1), (row, column + 1)):
                nr, nc = cell
                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] and cell not in seen:
                    seen.add(cell)
                    pending.append(cell)
        return False

    return sum(grid[row][column] == 1 and not escapes((row, column))
               for row in range(rows) for column in range(columns))


class EnclavePerCellEscapeTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before = [row[:] for row in grid]
        if expected is None:
            expected = each_land_cell_escape(grid)
        result = Solution().numEnclaves(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(grid, before)

    def test_all_small_binary_grids_against_each_cell_escape_search(self):
        checked = 0
        for rows, columns in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2),
                              (3, 3), (3, 4), (4, 3)):
            for values in product((0, 1), repeat=rows * columns):
                grid = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                self.check(grid)
                checked += 1
        self.assertEqual(checked, 8858)

    def test_maximum_grid_closed_land_boundary_bridge_and_thin_shapes(self):
        self.check([[1] * 500 for _ in range(500)], 0)
        grid = [[int(0 < row < 499 and 0 < column < 499) for column in range(500)]
                for row in range(500)]
        self.check(grid, 498 * 498)
        grid[0][250] = 1
        self.check(grid, 0)
        self.check([[1] * 500], 0)
        self.check([[1] for _ in range(500)], 0)


if __name__ == '__main__':
    unittest.main()
