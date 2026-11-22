import unittest

from python.p0059_spiral_matrix_ii import Solution


def directional_walk_matrix(n):
    output = [[0] * n for _ in range(n)]
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    row = column = direction = 0
    for value in range(1, n * n + 1):
        output[row][column] = value
        dr, dc = directions[direction]
        next_row, next_column = row + dr, column + dc
        if not (0 <= next_row < n and 0 <= next_column < n) or output[next_row][next_column]:
            direction = (direction + 1) % 4
            dr, dc = directions[direction]
            next_row, next_column = row + dr, column + dc
        row, column = next_row, next_column
    return output


class ShrinkingBoundarySpiralTests(unittest.TestCase):
    def test_every_legal_dimension_against_directional_walk(self):
        for n in range(1, 21):
            result = Solution().generateMatrix(n)
            self.assertIs(type(result), list)
            self.assertEqual(result, directional_walk_matrix(n))
            self.assertTrue(all(type(row) is list and len(row) == n for row in result))
            self.assertEqual(sorted(value for row in result for value in row), list(range(1, n * n + 1)))

    def test_known_turns_and_independent_output_storage(self):
        self.assertEqual(Solution().generateMatrix(1), [[1]])
        self.assertEqual(Solution().generateMatrix(2), [[1, 2], [4, 3]])
        self.assertEqual(Solution().generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
        for n in (2, 19, 20):
            first = Solution().generateMatrix(n)
            second = Solution().generateMatrix(n)
            self.assertEqual(len({id(row) for row in first}), n)
            before = [row[:] for row in second]
            first[0][0] = -1
            self.assertEqual(second, before)
            self.assertTrue(all(row[0] != -1 for row in first[1:]))


if __name__ == '__main__':
    unittest.main()
