import random
import unittest
from itertools import product

from python.p0749_contain_virus import Solution


def literal_components_edges_and_snapshot(grid):
    board, total = [row[:] for row in grid], 0
    rows, columns = len(board), len(board[0])
    while True:
        active = {(row, column) for row in range(rows) for column in range(columns) if board[row][column] == 1}
        if not active:
            return total
        parent = {cell: cell for cell in active}

        def find(cell):
            while parent[cell] != cell:
                cell = parent[cell]
            return cell

        for row, column in active:
            for neighbor in ((row + 1, column), (row, column + 1)):
                if neighbor in parent:
                    parent[find(neighbor)] = find((row, column))
        groups = {}
        for cell in active:
            groups.setdefault(find(cell), set()).add(cell)
        empty = {(row, column) for row in range(rows) for column in range(columns) if board[row][column] == 0}
        analyses = []
        for region in groups.values():
            edges = {(a, b) for a in region for b in empty if abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1}
            analyses.append((region, {b for _, b in edges}, len(edges)))
        maximum = max(len(frontier) for _, frontier, _ in analyses)
        if maximum == 0:
            return total
        choices = [index for index, (_, frontier, _) in enumerate(analyses) if len(frontier) == maximum]
        if len(choices) != 1:
            return None
        chosen = choices[0]
        total += analyses[chosen][2]
        blocked = analyses[chosen][0]
        remaining = set().union(*(region | frontier for index, (region, frontier, _) in enumerate(analyses) if index != chosen))
        board = [[-1 if board[row][column] == -1 or (row, column) in blocked else int((row, column) in remaining)
                  for column in range(columns)] for row in range(rows)]


class ContainVirusTests(unittest.TestCase):
    def check(self, grid, expected):
        before = [row[:] for row in grid]
        result = Solution().containVirus(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, grid)
        self.assertEqual(grid, before)

    def test_all_small_unique_threat_processes_and_seeded_boards_against_literal_edge_snapshots(self):
        examined = checked = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for values in product((0, 1), repeat=rows * columns):
                    grid = [list(values[start:start + columns]) for start in range(0, len(values), columns)]
                    expected = literal_components_edges_and_snapshot(grid)
                    examined += 1
                    if expected is not None:
                        self.check(grid, expected)
                        checked += 1
        self.assertEqual(examined, 682)
        self.assertGreater(checked, 100)
        rng, accepted = random.Random(749), 0
        for _ in range(2000):
            rows, columns = rng.randrange(4, 7), rng.randrange(4, 7)
            grid = [[rng.randrange(2) for _ in range(columns)] for _ in range(rows)]
            expected = literal_components_edges_and_snapshot(grid)
            if expected is not None:
                self.check(grid, expected)
                accepted += 1
                if accepted == 100:
                    break
        self.assertEqual(accepted, 100)

    def test_official_multiday_cases_shared_frontier_edges_and_fifty_square_boundaries(self):
        self.check([[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]], 10)
        self.check([[1,1,1],[1,0,1],[1,1,1]], 4)
        self.check([[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]], 13)
        self.check([[1,1],[1,0]], 2)
        self.check([[0] * 50 for _ in range(50)], 0)
        self.check([[1] * 50 for _ in range(50)], 0)
        hole = [[1] * 50 for _ in range(50)]
        hole[25][25] = 0
        self.check(hole, 4)
        single = [[0] * 50 for _ in range(50)]
        single[25][25] = 1
        self.check(single, 4)


if __name__ == '__main__':
    unittest.main()
