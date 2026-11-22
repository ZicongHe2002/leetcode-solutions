import unittest
from itertools import combinations, product

from python.p0785_is_graph_bipartite import Solution


def adjacency(size, edges):
    graph = [[] for _ in range(size)]
    for left, right in edges:
        graph[left].append(right)
        graph[right].append(left)
    return graph


class BipartiteTests(unittest.TestCase):
    def check(self, graph, expected):
        before = [neighbors[:] for neighbors in graph]
        identities = [id(neighbors) for neighbors in graph]
        result = Solution().isBipartite(graph)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(graph, before)
        self.assertEqual([id(neighbors) for neighbors in graph], identities)

    def test_all_small_undirected_graphs_against_full_binary_colorings(self):
        checks = 0
        for size in range(6):
            possible_edges = list(combinations(range(size), 2))
            for mask in range(1 << len(possible_edges)):
                edges = [edge for bit, edge in enumerate(possible_edges) if mask & (1 << bit)]
                expected = any(all(colors[left] != colors[right] for left, right in edges)
                               for colors in product((0, 1), repeat=size))
                self.check(adjacency(size, edges), expected)
                checks += 1
        self.assertEqual(checks, 1100)

    def test_maximum_even_odd_cycles_disconnected_and_complete_bipartite(self):
        self.check(adjacency(100, [(node, (node + 1) % 100) for node in range(100)]), True)
        self.check(adjacency(100, [(node, (node + 1) % 99) for node in range(99)]), False)
        self.check(adjacency(100, [(left, right) for left in range(50) for right in range(50, 100)]), True)
        self.check(adjacency(100, [(0, 1), (1, 2), (0, 2)]), False)
        self.check(adjacency(100, [(node, node + 1) for node in range(99)]), True)


if __name__ == '__main__':
    unittest.main()
