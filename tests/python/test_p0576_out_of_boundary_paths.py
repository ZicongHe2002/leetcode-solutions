from functools import lru_cache
import unittest

from python.p0576_out_of_boundary_paths import Solution


def enumerate_paths(rows, columns, moves, row, column):
    if not (0 <= row < rows and 0 <= column < columns):
        return 1
    if moves == 0:
        return 0
    return sum(enumerate_paths(rows, columns, moves - 1, row + dr, column + dc)
               for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))


def exact_count(rows, columns, moves, row, column):
    @lru_cache(None)
    def visit(left, r, c):
        if not (0 <= r < rows and 0 <= c < columns):
            return 1
        if left == 0:
            return 0
        return sum(visit(left - 1, r + dr, c + dc)
                   for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    return visit(moves, row, column)


class BoundaryPathTests(unittest.TestCase):
    def check(self, rows, columns, moves, row, column, expected):
        result = Solution().findPaths(rows, columns, moves, row, column)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertTrue(0 <= result < 10**9 + 7)

    def test_all_small_starts_and_budgets_against_direction_enumeration(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for row in range(rows):
                    for column in range(columns):
                        for moves in range(7):
                            self.check(rows, columns, moves, row, column,
                                       enumerate_paths(rows, columns, moves, row, column))
                            checks += 1
        self.assertEqual(checks, 252)

    def test_fifty_moves_exact_unmodded_counts_and_degenerate_grids(self):
        for rows, columns, row, column in ((50, 50, 25, 25), (50, 50, 0, 0), (1, 50, 0, 25)):
            exact = exact_count(rows, columns, 50, row, column)
            self.assertGreater(exact, 10**9 + 7)
            self.check(rows, columns, 50, row, column, exact % (10**9 + 7))
        self.check(1, 1, 50, 0, 0, 4)
        self.check(50, 50, 0, 0, 0, 0)
        self.check(2, 2, 2, 0, 0, 6)
        self.check(1, 3, 3, 0, 1, 12)


if __name__ == '__main__':
    unittest.main()
