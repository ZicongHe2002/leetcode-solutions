from itertools import combinations
import unittest

from python.p1971_find_if_path_exists_in_graph import Solution


def undirected_transitive_closure(n, edges):
    reachable = [[left == right for right in range(n)] for left in range(n)]
    for left, right in edges:
        reachable[left][right] = reachable[right][left] = True
    for via in range(n):
        for left in range(n):
            for right in range(n):
                reachable[left][right] |= reachable[left][via] and reachable[via][right]
    return reachable


class IterativeUndirectedReachabilityTests(unittest.TestCase):
    def check(self, n, edges, source, destination, expected):
        before = [pair[:] for pair in edges]
        result = Solution().validPath(n, edges, source, destination)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(edges, before)

    def test_all_small_undirected_graphs_and_every_endpoint_pair(self):
        graphs = queries = 0
        for n in range(1, 6):
            possible = list(combinations(range(n), 2))
            for mask in range(1 << len(possible)):
                edges = [list(pair) for index, pair in enumerate(possible) if mask >> index & 1]
                reference = undirected_transitive_closure(n, edges)
                for source in range(n):
                    for destination in range(n):
                        self.check(n, edges, source, destination, reference[source][destination])
                        queries += 1
                graphs += 1
        self.assertEqual((graphs, queries), (1099, 26705))

    def test_maximum_nodes_edges_long_chain_disconnection_and_singleton(self):
        n = 200000
        chain = [[node, node + 1] for node in range(n - 1)]
        self.check(n, chain, 0, n - 1, True)
        disconnected = [[node, node + 1] for node in range(n - 1) if node != n // 2 - 1]
        self.check(n, disconnected, 0, n - 1, False)
        self.check(n, chain + [[n - 1, 0]], 0, n // 2, True)
        self.check(n, [], 0, n - 1, False)
        self.check(1, [], 0, 0, True)


if __name__ == '__main__':
    unittest.main()
