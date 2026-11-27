from collections import deque
from functools import lru_cache
from itertools import combinations, permutations
import unittest

from python.p0573_squirrel_simulation import Solution


@lru_cache(None)
def grid_distances(rows, columns, start):
    distances = {start: 0}
    pending = deque([start])
    while pending:
        row, column = pending.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (row + dr, column + dc)
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < columns
                    and neighbor not in distances):
                distances[neighbor] = distances[(row, column)] + 1
                pending.append(neighbor)
    return distances


def all_collection_orders(rows, columns, tree, squirrel, nuts):
    costs = []
    for order in permutations(nuts):
        position, cost = squirrel, 0
        for nut in order:
            cost += grid_distances(rows, columns, position)[nut]
            cost += grid_distances(rows, columns, nut)[tree]
            position = tree
        costs.append(cost)
    return min(costs)


class SquirrelTests(unittest.TestCase):
    def check(self, height, width, tree, squirrel, nuts, expected):
        before = (tree[:], squirrel[:], [nut[:] for nut in nuts])
        result = Solution().minDistance(height, width, tree, squirrel, nuts)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual((tree, squirrel, nuts), before)

    def test_small_gardens_against_grid_bfs_and_all_collection_orders(self):
        checks = 0
        for rows, columns in ((1, 3), (2, 3), (3, 3)):
            cells = [(r, c) for r in range(rows) for c in range(columns)]
            for tree, squirrel in permutations(cells, 2):
                available = [cell for cell in cells if cell not in (tree, squirrel)]
                for size in range(1, min(3, len(available)) + 1):
                    for nuts in combinations(available, size):
                        expected = all_collection_orders(rows, columns, tree, squirrel, nuts)
                        self.check(rows, columns, list(tree), list(squirrel), list(map(list, nuts)), expected)
                        checks += 1
        self.assertEqual(checks, 4962)

    def test_maximum_nuts_negative_saving_and_examples(self):
        nuts = [[row, column] for row in range(100) for column in range(50)]
        self.check(100, 100, [0, 99], [99, 99], nuts, 1239901)
        self.check(1, 3, [0, 1], [0, 0], [[0, 2]], 3)
        self.check(3, 3, [1, 1], [1, 1], [[0, 0], [2, 2]], 8)
        self.check(5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]], 12)


if __name__ == '__main__':
    unittest.main()
