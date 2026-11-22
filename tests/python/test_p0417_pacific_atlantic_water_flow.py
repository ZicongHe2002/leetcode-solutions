import unittest
from itertools import product

from python.p0417_pacific_atlantic_water_flow import Solution


def direct_downhill_positions(heights):
    rows, columns = len(heights), len(heights[0])
    result = []
    for start_row in range(rows):
        for start_column in range(columns):
            visited = {(start_row, start_column)}
            pending = [(start_row, start_column)]
            pacific = atlantic = False
            while pending:
                row, column = pending.pop()
                pacific |= row == 0 or column == 0
                atlantic |= row == rows - 1 or column == columns - 1
                if pacific and atlantic:
                    break
                for next_row, next_column in [(row - 1, column), (row + 1, column),
                                               (row, column - 1), (row, column + 1)]:
                    if 0 <= next_row < rows and 0 <= next_column < columns:
                        position = (next_row, next_column)
                        if position not in visited and heights[next_row][next_column] <= heights[row][column]:
                            visited.add(position)
                            pending.append(position)
            if pacific and atlantic:
                result.append([start_row, start_column])
    return result


class OceanFlowTests(unittest.TestCase):
    def check(self, heights, expected=None):
        before = [row[:] for row in heights]
        identities = [id(row) for row in heights]
        if expected is None:
            expected = direct_downhill_positions(heights)
        result = Solution().pacificAtlantic(heights)
        self.assertEqual(result, expected)
        self.assertEqual(len({tuple(position) for position in result}), len(result))
        self.assertEqual(heights, before)
        self.assertEqual([id(row) for row in heights], identities)

    def test_all_small_height_grids_against_direct_downhill_walks(self):
        checks = 0
        for rows, columns in [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)]:
            alphabet = range(2) if rows == columns == 3 else range(3)
            for values in product(alphabet, repeat=rows * columns):
                grid = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                self.check(grid)
                checks += 1
        self.assertEqual(checks, 2072)

    def test_maximum_plateaus_monotone_boundaries_single_rows_and_columns(self):
        all_positions = [[row, column] for row in range(200) for column in range(200)]
        self.check([[100000] * 200 for _ in range(200)], all_positions)
        self.check([[row + column for column in range(200)] for row in range(200)],
                   [[row, column] for row in range(200) for column in range(200) if row == 199 or column == 199])
        self.check([[100000 - row - column for column in range(200)] for row in range(200)],
                   [[row, column] for row in range(200) for column in range(200) if row == 0 or column == 0])
        self.check([list(range(200))], [[0, column] for column in range(200)])
        self.check([[row] for row in range(200)], [[row, 0] for row in range(200)])


if __name__ == '__main__':
    unittest.main()
