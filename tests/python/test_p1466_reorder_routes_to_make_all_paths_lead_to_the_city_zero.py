from itertools import product
import unittest

from python.p1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero import Solution


def tree_from_prufer(n, code):
    degree = [1] * n
    for node in code:
        degree[node] += 1
    edges = []
    for node in code:
        leaf = next(index for index in range(n) if degree[index] == 1)
        edges.append((leaf, node))
        degree[leaf] -= 1
        degree[node] -= 1
    edges.append(tuple(index for index in range(n) if degree[index] == 1))
    return edges


def every_reversed_edge_subset(n, connections):
    best = len(connections) + 1
    for mask in range(1 << len(connections)):
        cost = mask.bit_count()
        incoming = [[] for _ in range(n)]
        for index, (source, target) in enumerate(connections):
            if mask >> index & 1:
                source, target = target, source
            incoming[target].append(source)
        reachable = {0}
        pending = [0]
        for node in pending:
            for predecessor in incoming[node]:
                if predecessor not in reachable:
                    reachable.add(predecessor)
                    pending.append(predecessor)
        if len(reachable) == n:
            best = min(best, cost)
    return best


class RootwardTreeReversalTests(unittest.TestCase):
    def check(self, n, connections, expected=None):
        before = [pair[:] for pair in connections]
        if expected is None:
            expected = every_reversed_edge_subset(n, connections)
        result = Solution().minReorder(n, connections)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(connections, before)

    def test_all_small_labeled_trees_and_each_edge_orientation(self):
        checks = 0
        for n in range(2, 6):
            for code in product(range(n), repeat=n - 2):
                tree = tree_from_prufer(n, code)
                for orientation in range(1 << (n - 1)):
                    connections = [[right, left] if orientation >> index & 1 else [left, right]
                                   for index, (left, right) in enumerate(tree)]
                    self.check(n, connections)
                    checks += 1
        self.assertEqual(checks, 2142)

    def test_maximum_length_chains_star_and_known_mixed_directions(self):
        n = 50000
        self.check(n, [[node, node + 1] for node in range(n - 1)], n - 1)
        self.check(n, [[node + 1, node] for node in range(n - 1)], 0)
        self.check(n, [[node, node + 1] if node % 2 == 0 else [node + 1, node]
                       for node in range(n - 1)], 25000)
        self.check(n, [[0, node] for node in range(1, n)], n - 1)
        self.check(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]], 3)


if __name__ == '__main__':
    unittest.main()
