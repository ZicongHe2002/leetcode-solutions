from itertools import product
import unittest

from python.p0310_minimum_height_trees import Solution


def tree_from_prufer(n, code):
    degrees = [1] * n
    for node in code:
        degrees[node] += 1
    edges = []
    for node in code:
        leaf = next(index for index in range(n) if degrees[index] == 1)
        edges.append([leaf, node])
        degrees[leaf] -= 1
        degrees[node] -= 1
    edges.append([index for index in range(n) if degrees[index] == 1])
    return edges


def every_root_height_reference(n, edges):
    neighbors = [[] for _ in range(n)]
    for left, right in edges:
        neighbors[left].append(right)
        neighbors[right].append(left)
    heights = []
    for root in range(n):
        distance = {root: 0}
        pending = [root]
        for node in pending:
            for neighbor in neighbors[node]:
                if neighbor not in distance:
                    distance[neighbor] = distance[node] + 1
                    pending.append(neighbor)
        heights.append(max(distance.values()))
    return {root for root, height in enumerate(heights) if height == min(heights)}


class LayeredTreeCenterTests(unittest.TestCase):
    def check(self, n, edges, expected=None):
        before = [pair[:] for pair in edges]
        if expected is None:
            expected = every_root_height_reference(n, edges)
        result = Solution().findMinHeightTrees(n, edges)
        self.assertIs(type(result), list)
        self.assertEqual(set(result), set(expected))
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(edges, before)

    def test_all_small_labeled_trees_against_every_root_height(self):
        self.check(1, [])
        checks = 1
        for n in range(2, 7):
            for code in product(range(n), repeat=n - 2):
                self.check(n, tree_from_prufer(n, code))
                checks += 1
        self.assertEqual(checks, 1442)

    def test_maximum_chain_parity_stars_and_extreme_center_labels(self):
        self.check(20000, [[node, node + 1] for node in range(19999)], {9999, 10000})
        self.check(19999, [[node, node + 1] for node in range(19998)], {9999})
        self.check(20000, [[0, node] for node in range(1, 20000)], {0})
        self.check(20000, [[node, 19999] for node in range(19999)], {19999})


if __name__ == '__main__':
    unittest.main()
