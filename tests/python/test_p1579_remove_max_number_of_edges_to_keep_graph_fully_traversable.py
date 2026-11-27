from itertools import combinations
import unittest

from python.p1579_remove_max_number_of_edges_to_keep_graph_fully_traversable import Solution


def best_kept_subset(size, edges):
    def connected(mask, allowed):
        adjacency = [[] for _ in range(size)]
        for index, (kind, first, second) in enumerate(edges):
            if mask >> index & 1 and kind in allowed:
                adjacency[first - 1].append(second - 1)
                adjacency[second - 1].append(first - 1)
        seen, pending = {0}, [0]
        while pending:
            for neighbor in adjacency[pending.pop()]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        return len(seen) == size

    best = len(edges) + 1
    for mask in range(1 << len(edges)):
        kept = mask.bit_count()
        if kept < best and connected(mask, (1, 3)) and connected(mask, (2, 3)):
            best = kept
    return -1 if best > len(edges) else len(edges) - best


class SharedEdgeOptimalityTests(unittest.TestCase):
    def check(self, size, edges, expected=None):
        before = [edge[:] for edge in edges]
        if expected is None:
            expected = best_kept_subset(size, edges)
        result = Solution().maxNumEdgesToRemove(size, edges)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(edges, before)

    def test_every_small_nonempty_typed_graph_against_all_kept_subsets(self):
        checks = 0
        for size in (2, 3):
            possible = [(kind, first, second) for kind in (1, 2, 3)
                        for first, second in combinations(range(1, size + 1), 2)]
            for mask in range(1, 1 << len(possible)):
                edges = [list(edge) for index, edge in enumerate(possible) if mask >> index & 1]
                self.check(size, edges)
                checks += 1
        self.assertEqual(checks, 518)

    def test_maximum_nodes_edges_shared_cycles_and_missing_bob_connectivity(self):
        shared = [[3, index, index + 1] for index in range(1, 100000)]
        self.check(100000, shared + [[3, 1, 3]], 1)
        self.check(100000, [[1, index, index + 1] for index in range(1, 100000)], -1)
        shared = [[3, index, index + 1] for index in range(1, 99999)]
        self.check(99999, shared + [[1, 1, 2], [2, 1, 2]], 2)


if __name__ == '__main__':
    unittest.main()
