import random
import unittest
from itertools import combinations, permutations

from python.p0685_redundant_connection_ii import Solution


def is_rooted_tree(edges, omitted):
    n = len(edges)
    incoming, children = [0] * (n + 1), [[] for _ in range(n + 1)]
    for index, (source, target) in enumerate(edges):
        if index != omitted:
            incoming[target] += 1
            children[source].append(target)
    roots = [node for node in range(1, n + 1) if incoming[node] == 0]
    if len(roots) != 1 or any(incoming[node] != 1 for node in range(1, n + 1) if node != roots[0]):
        return False
    seen, pending = set(), roots[:]
    while pending:
        node = pending.pop()
        if node in seen:
            return False
        seen.add(node)
        pending.extend(children[node])
    return len(seen) == n


def remove_edges_by_definition(edges):
    for omitted in range(len(edges) - 1, -1, -1):
        if is_rooted_tree(edges, omitted):
            return list(edges[omitted])
    return None


class RedundantDirectedEdgeTests(unittest.TestCase):
    def check(self, edges, expected=None):
        before = [edge[:] for edge in edges]
        ids = [id(edge) for edge in edges]
        if expected is None:
            expected = remove_edges_by_definition(edges)
        result = Solution().findRedundantDirectedConnection(edges)
        self.assertIs(type(result), list)
        self.assertEqual(result, expected, edges[:10])
        self.assertEqual(edges, before)
        self.assertEqual([id(edge) for edge in edges], ids)

    def test_all_small_legal_directed_graphs_and_edge_orders_against_tree_definition(self):
        for n in (3, 4):
            possible = [(source, target) for source in range(1, n + 1)
                        for target in range(1, n + 1) if source != target]
            for selected in combinations(possible, n):
                if remove_edges_by_definition(selected) is None:
                    continue
                for order in permutations(selected):
                    self.check([list(edge) for edge in order])

    def test_seeded_rooted_trees_and_thousand_node_conflict_cycle_cases(self):
        rng = random.Random(685)
        for _ in range(200):
            n = rng.randrange(3, 16)
            labels = list(range(1, n + 1))
            rng.shuffle(labels)
            tree = [(labels[rng.randrange(i)], labels[i]) for i in range(1, n)]
            extra = rng.choice([(a, b) for a in labels for b in labels if a != b and (a, b) not in tree])
            edges = [list(edge) for edge in tree + [extra]]
            rng.shuffle(edges)
            self.check(edges)
        chain = [[i, i + 1] for i in range(1, 1000)]
        self.check(chain + [[1000, 1]], [1000, 1])
        self.check([[1, 1000]] + chain, [999, 1000])
        both = [[2, 1], [3, 1], [1, 2]] + [[i, i + 1] for i in range(3, 1000)]
        self.assertEqual(len(both), 1000)
        self.check(both, [2, 1])


if __name__ == '__main__':
    unittest.main()
