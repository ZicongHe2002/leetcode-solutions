import unittest
from itertools import combinations, permutations

from python.p0684_redundant_connection import Solution


def is_connected(size, edges):
    graph = [[] for _ in range(size + 1)]
    for left, right in edges:
        graph[left].append(right)
        graph[right].append(left)
    visited, pending = {1}, [1]
    while pending:
        for neighbor in graph[pending.pop()]:
            if neighbor not in visited:
                visited.add(neighbor)
                pending.append(neighbor)
    return len(visited) == size


class RedundantEdgeTests(unittest.TestCase):
    def check(self, edges):
        before = [edge[:] for edge in edges]
        expected = next(edges[index] for index in range(len(edges) - 1, -1, -1)
                        if is_connected(len(edges), edges[:index] + edges[index + 1:]))
        self.assertEqual(Solution().findRedundantConnection(edges), expected)
        self.assertEqual(edges, before)

    def test_all_small_unicyclic_graphs_and_edge_orders_against_edge_removal(self):
        checks = 0
        for size in range(3, 6):
            possible_edges = list(combinations(range(1, size + 1), 2))
            for edges in combinations(possible_edges, size):
                if not is_connected(size, edges):
                    continue
                for order in permutations(edges):
                    self.check([list(edge) for edge in order])
                    checks += 1
        self.assertEqual(checks, 27006)

    def test_maximum_cycle_reordered_closure_and_bridge_after_cycle(self):
        chain = [[node, node + 1] for node in range(1, 1000)]
        self.check(chain + [[1, 1000]])
        self.check([[1, 1000]] + chain)
        self.check([[1, 2], [2, 3], [1, 3], [3, 4]])


if __name__ == '__main__':
    unittest.main()
