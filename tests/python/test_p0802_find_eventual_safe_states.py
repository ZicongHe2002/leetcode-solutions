import unittest

from python.p0802_find_eventual_safe_states import Solution


def closure_cycle_reference(graph):
    size = len(graph)
    reachable = [[target in graph[source] for target in range(size)] for source in range(size)]
    for via in range(size):
        for source in range(size):
            for target in range(size):
                reachable[source][target] |= reachable[source][via] and reachable[via][target]
    cyclic = [node for node in range(size) if reachable[node][node]]
    return [source for source in range(size) if not any(reachable[source][node] for node in cyclic)]


class ReverseTerminalEliminationTests(unittest.TestCase):
    def check(self, graph, expected=None):
        before = [neighbors[:] for neighbors in graph]
        if expected is None:
            expected = closure_cycle_reference(graph)
        result = Solution().eventualSafeNodes(graph)
        self.assertIs(type(result), list)
        self.assertEqual(result, expected)
        self.assertEqual(result, sorted(set(result)))
        self.assertEqual(graph, before)

    def test_all_small_nonempty_edge_graphs_including_self_loops(self):
        checks = 0
        for size in range(1, 4):
            for mask in range(1, 1 << (size * size)):
                graph = [[target for target in range(size) if mask >> (source * size + target) & 1]
                         for source in range(size)]
                self.check(graph)
                checks += 1
        self.assertEqual(checks, 527)

    def test_maximum_nodes_edges_long_chains_and_mixed_components(self):
        size = 10000
        self.check([[node + 1] for node in range(size - 1)] + [[]], list(range(size)))
        self.check([[(node + 1) % size] for node in range(size)], [])
        mixed = [[(node + 1) % 5000] for node in range(5000)]
        mixed += [[node + 1] for node in range(5000, size - 1)] + [[]]
        self.check(mixed, list(range(5000, size)))
        cyclic = [sorted((node + step) % size for step in range(1, 5)) for node in range(size)]
        self.assertEqual(sum(map(len, cyclic)), 40000)
        self.check(cyclic, [])
        acyclic = [list(range(node + 1, min(size, node + 5))) for node in range(size)]
        acyclic[0].extend(range(5, 15))
        self.assertEqual(sum(map(len, acyclic)), 40000)
        self.check(acyclic, list(range(size)))


if __name__ == '__main__':
    unittest.main()
