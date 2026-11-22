import heapq
from itertools import combinations, product
import unittest

from python.p1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance import Solution


def separate_source_heap_reference(n, edges, threshold):
    neighbors = [[] for _ in range(n)]
    for left, right, weight in edges:
        neighbors[left].append((right, weight))
        neighbors[right].append((left, weight))
    counts = []
    for source in range(n):
        distance = [float('inf')] * n
        distance[source] = 0
        pending = [(0, source)]
        while pending:
            cost, node = heapq.heappop(pending)
            if cost != distance[node]:
                continue
            for target, weight in neighbors[node]:
                candidate = cost + weight
                if candidate < distance[target]:
                    distance[target] = candidate
                    heapq.heappush(pending, (candidate, target))
        counts.append(sum(node != source and cost <= threshold for node, cost in enumerate(distance)))
    return min(range(n), key=lambda city: (counts[city], -city))


class ThresholdAllPairsCityTests(unittest.TestCase):
    def check(self, n, edges, threshold, expected=None):
        before = [edge[:] for edge in edges]
        if expected is None:
            expected = separate_source_heap_reference(n, edges, threshold)
        result = Solution().findTheCity(n, edges, threshold)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(edges, before)

    def test_all_small_nonempty_weighted_graphs_and_thresholds(self):
        graphs = checks = 0
        for n in range(2, 5):
            possible = list(combinations(range(n), 2))
            for weights in product((0, 1, 3), repeat=len(possible)):
                edges = [[left, right, weight] for (left, right), weight in zip(possible, weights) if weight]
                if not edges:
                    continue
                for threshold in (1, 2, 3, 4, 6, 10000):
                    self.check(n, edges, threshold)
                    checks += 1
                graphs += 1
        self.assertEqual((graphs, checks), (756, 4536))

    def test_maximum_nodes_edges_threshold_equality_and_tie_direction(self):
        complete = [[left, right, 10000] for left, right in combinations(range(100), 2)]
        self.assertEqual(len(complete), 4950)
        self.check(100, complete, 9999, 99)
        self.check(100, complete, 10000, 99)
        self.check(100, [[node, node + 1, 1] for node in range(1, 99)], 10000, 0)
        self.check(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4, 3)


if __name__ == '__main__':
    unittest.main()
