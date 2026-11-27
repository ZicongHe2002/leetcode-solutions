import unittest

from python.p0505_the_maze_ii import Solution


def maximal_segment_weighted_edges(maze):
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
                if member > start:
                    edges[row, member].append(((row, start), member - start))
                if member < column - 1:
                    edges[row, member].append(((row, column - 1), column - 1 - member))
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
                if member > start:
                    edges[member, column].append(((start, column), member - start))
                if member < row - 1:
                    edges[member, column].append(((row - 1, column), row - 1 - member))
    return edges


def bounded_distance_relaxation(edges, origin):
    distances = {origin: 0}
    for _ in range(len(edges) - 1):
        following = dict(distances)
        for current, distance in distances.items():
            for target, weight in edges[current]:
                candidate = distance + weight
                if target not in following or candidate < following[target]:
                    following[target] = candidate
        if following == distances:
            break
        distances = following
    return distances


class RollingWeightedDistanceTests(unittest.TestCase):
    def check(self, maze, start, destination, expected):
        before = ([row[:] for row in maze], start[:], destination[:])
        actual = Solution().shortestDistance(maze, start, destination)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected)
        self.assertEqual((maze, start, destination), before)

    def test_all_three_by_three_wall_layouts_and_distinct_empty_endpoints(self):
        layouts = queries = 0
        for mask in range(1 << 9):
            maze = [[(mask >> (3 * row + column)) & 1 for column in range(3)] for row in range(3)]
            edges = maximal_segment_weighted_edges(maze)
            layouts += 1
            for origin in edges:
                expected = bounded_distance_relaxation(edges, origin)
                for target in edges:
                    if origin != target:
                        self.check(maze, list(origin), list(target), expected.get(target, -1))
                        queries += 1
        self.assertEqual((layouts, queries), (512, 9216))

    def test_maximum_grid_corridor_stops_and_branching_distance(self):
        maze = [[0] * 100 for _ in range(100)]
        self.check(maze, [0, 0], [99, 99], 198)
        self.check(maze, [0, 0], [0, 50], -1)
        self.check([[0] * 100], [0, 0], [0, 99], 99)
        self.check([[0] * 100], [0, 0], [0, 50], -1)
        self.check([[0, 1, 0]], [0, 0], [0, 2], -1)
        self.check([[0, 0]], [0, 0], [0, 0], 0)
        maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
                [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
        self.check(maze, [0, 4], [4, 4], 12)
        self.check(maze, [0, 4], [3, 2], -1)


if __name__ == '__main__':
    unittest.main()
