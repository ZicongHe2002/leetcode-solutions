import unittest
from itertools import product

from python.p0743_network_delay_time import Solution


def floyd_network_delay(times, length, source):
    infinity = float('inf')
    distance = [[infinity] * length for _ in range(length)]
    for node in range(length):
        distance[node][node] = 0
    for first, second, weight in times:
        distance[first - 1][second - 1] = weight
    for middle in range(length):
        for first in range(length):
            for second in range(length):
                distance[first][second] = min(distance[first][second], distance[first][middle] + distance[middle][second])
    result = max(distance[source - 1])
    return -1 if result == infinity else result


class NetworkDelayTests(unittest.TestCase):
    def check(self, times, length, source, expected=None):
        before = [edge[:] for edge in times]
        if expected is None:
            expected = floyd_network_delay(times, length, source)
        result = Solution().networkDelayTime(times, length, source)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(times, before)

    def test_all_small_nonnegative_graphs_against_floyd(self):
        edges = [(first, second) for first in range(1, 4) for second in range(1, 4) if first != second]
        graphs = checks = 0
        for weights in product((-1, 0, 2), repeat=len(edges)):
            times = [[first, second, weight] for (first, second), weight in zip(edges, weights) if weight >= 0]
            graphs += 1
            for source in range(1, 4):
                self.check(times, 3, source)
                checks += 1
        self.assertEqual((graphs, checks), (729, 2187))

    def test_maximum_nodes_edges_zero_weights_unreachable_and_stale_entries(self):
        self.check([[node, node + 1, 100] for node in range(1, 100)], 100, 1, 9900)
        self.check([[node, node + 1, 0] for node in range(1, 100)], 100, 1, 0)
        dense = [[first, second, 100] for first in range(1, 101) for second in range(1, 101) if first != second][:6000]
        self.assertEqual(len(dense), 6000)
        self.check(dense, 100, 1, 100)
        self.check(dense, 100, 100, -1)
        self.check([[1, 2, 10], [1, 3, 1], [3, 2, 1], [2, 4, 1], [3, 4, 50]], 4, 1, 3)
        self.check([], 1, 1, 0)
        self.check([], 100, 1, -1)


if __name__ == '__main__':
    unittest.main()
