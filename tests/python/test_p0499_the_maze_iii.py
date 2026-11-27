import unittest

from python.p0499_the_maze_iii import Solution


def segment_edges_with_hole(maze, hole):
    rows, columns = len(maze), len(maze[0])
    edges = {(row, column): [] for row in range(rows) for column in range(columns) if maze[row][column] == 0}
    for row in range(rows):
        column = 0
        while column < columns:
            if maze[row][column]:
                column += 1
                continue
            start = column
            while column < columns and maze[row][column] == 0:
                column += 1
            for member in range(start, column):
                if (row, member) == hole:
                    continue
                left = hole[1] if hole[0] == row and start <= hole[1] < member else start
                right = hole[1] if hole[0] == row and member < hole[1] < column else column - 1
                if left < member:
                    edges[row, member].append(((row, left), member - left, 'l'))
                if right > member:
                    edges[row, member].append(((row, right), right - member, 'r'))
    for column in range(columns):
        row = 0
        while row < rows:
            if maze[row][column]:
                row += 1
                continue
            start = row
            while row < rows and maze[row][column] == 0:
                row += 1
            for member in range(start, row):
                if (member, column) == hole:
                    continue
                up = hole[0] if hole[1] == column and start <= hole[0] < member else start
                down = hole[0] if hole[1] == column and member < hole[0] < row else row - 1
                if up < member:
                    edges[member, column].append(((up, column), member - up, 'u'))
                if down > member:
                    edges[member, column].append(((down, column), down - member, 'd'))
    return edges


def bounded_relaxation_oracle(edges, origin, hole):
    best = {origin: (0, '')}
    for _ in range(len(edges) - 1):
        following = dict(best)
        for current, (distance, path) in best.items():
            for target, weight, letter in edges[current]:
                candidate = (distance + weight, path + letter)
                if target not in following or candidate < following[target]:
                    following[target] = candidate
        if following == best:
            break
        best = following
    return best[hole][1] if hole in best else 'impossible'


class MazeHoleLexicographicTests(unittest.TestCase):
    def check(self, maze, ball, hole, expected):
        before = ([row[:] for row in maze], ball[:], hole[:])
        actual = Solution().findShortestWay(maze, ball, hole)
        self.assertIs(type(actual), str)
        self.assertEqual(actual, expected)
        self.assertTrue(actual == 'impossible' or set(actual) <= set('dlru'))
        self.assertEqual((maze, ball, hole), before)

    def test_every_three_by_three_layout_and_distinct_ball_hole_against_relaxation(self):
        layouts = queries = 0
        for mask in range(1 << 9):
            maze = [[(mask >> (3 * row + column)) & 1 for column in range(3)] for row in range(3)]
            points = [(row, column) for row in range(3) for column in range(3) if maze[row][column] == 0]
            layouts += 1
            for hole in points:
                edges = segment_edges_with_hole(maze, hole)
                for ball in points:
                    if ball != hole:
                        self.check(maze, list(ball), list(hole), bounded_relaxation_oracle(edges, ball, hole))
                        queries += 1
        self.assertEqual((layouts, queries), (512, 9216))

    def test_maximum_grid_distance_ties_hole_capture_and_zero_step_rejection(self):
        maze = [[0] * 100 for _ in range(100)]
        self.check(maze, [99, 99], [0, 0], 'lu')
        self.check(maze, [99, 99], [0, 50], 'ul')
        self.check(maze, [0, 0], [50, 50], 'impossible')
        self.check([[0] * 100], [0, 0], [0, 50], 'r')
        self.check([[0, 0]], [0, 0], [0, 1], 'r')
        self.check([[0, 1, 0]], [0, 0], [0, 2], 'impossible')
        self.check([[0, 0]], [0, 0], [0, 0], '')


if __name__ == '__main__':
    unittest.main()
