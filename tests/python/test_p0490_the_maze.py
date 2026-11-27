import unittest

from python.p0490_the_maze import Solution


def maximal_segment_graph(maze):
    rows, columns = len(maze), len(maze[0])
    edges = {(row, column): set() for row in range(rows) for column in range(columns) if maze[row][column] == 0}
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
                edges[row, member].update(((row, start), (row, column - 1)))
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
                edges[member, column].update(((start, column), (row - 1, column)))
    return edges


def reachable_stops(edges, origin):
    reached, pending = {origin}, [origin]
    while pending:
        current = pending.pop()
        for following in edges[current] - reached:
            reached.add(following)
            pending.append(following)
    return reached


class RollingStopGraphTests(unittest.TestCase):
    def check(self, maze, start, destination, expected):
        before = ([row[:] for row in maze], start[:], destination[:])
        actual = Solution().hasPath(maze, start, destination)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, expected)
        self.assertEqual((maze, start, destination), before)

    def test_every_three_by_three_wall_layout_and_distinct_empty_endpoints(self):
        layouts = queries = 0
        for mask in range(1 << 9):
            maze = [[(mask >> (3 * row + column)) & 1 for column in range(3)] for row in range(3)]
            edges = maximal_segment_graph(maze)
            layouts += 1
            for origin in edges:
                reachable = reachable_stops(edges, origin)
                for target in edges:
                    if origin != target:
                        self.check(maze, list(origin), list(target), target in reachable)
                        queries += 1
        self.assertEqual((layouts, queries), (512, 9216))

    def test_maximum_rectangle_corridor_pass_through_and_isolation(self):
        maze = [[0] * 100 for _ in range(100)]
        self.check(maze, [0, 0], [99, 99], True)
        self.check(maze, [0, 0], [0, 50], False)
        self.check([[0] * 100], [0, 0], [0, 99], True)
        self.check([[0] * 100], [0, 0], [0, 50], False)
        self.check([[0, 1, 0]], [0, 0], [0, 2], False)
        self.check([[0, 0]], [0, 0], [0, 0], True)
        maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
                [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
        self.check(maze, [0, 4], [4, 4], True)
        self.check(maze, [0, 4], [3, 2], False)


if __name__ == '__main__':
    unittest.main()
