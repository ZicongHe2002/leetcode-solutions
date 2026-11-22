from collections import deque
from itertools import combinations
import unittest

from python.p1319_number_of_operations_to_make_network_connected import Solution


def rewire_distances(size, possible):
    def connected(mask):
        adjacency = [[] for _ in range(size)]
        for index, (first, second) in enumerate(possible):
            if mask >> index & 1:
                adjacency[first].append(second)
                adjacency[second].append(first)
        seen, pending = {0}, [0]
        while pending:
            for neighbor in adjacency[pending.pop()]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        return len(seen) == size

    distances = {mask: 0 for mask in range(1 << len(possible)) if connected(mask)}
    queue = deque(distances)
    while queue:
        mask = queue.popleft()
        for removed in range(len(possible)):
            if not (mask >> removed & 1):
                continue
            for added in range(len(possible)):
                if mask >> added & 1:
                    continue
                following = mask ^ (1 << removed) ^ (1 << added)
                if following not in distances:
                    distances[following] = distances[mask] + 1
                    queue.append(following)
    return distances


class NetworkRewiringTests(unittest.TestCase):
    def check(self, size, edges, expected):
        before = [edge[:] for edge in edges]
        result = Solution().makeConnected(size, edges)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(edges, before)

    def test_every_small_nonempty_graph_against_rewire_state_bfs(self):
        checks = 0
        for size in range(2, 6):
            possible = list(combinations(range(size), 2))
            distances = rewire_distances(size, possible)
            for mask in range(1, 1 << len(possible)):
                edges = [list(edge) for index, edge in enumerate(possible) if mask >> index & 1]
                self.check(size, edges, distances.get(mask, -1))
                checks += 1
        self.assertEqual(checks, 1094)

    def test_maximum_nodes_edges_and_redundancy_for_an_isolated_node(self):
        chain = [[index, index + 1] for index in range(99999)]
        self.check(100000, chain, 0)
        self.check(100000, chain + [[0, 2]], 0)
        self.check(100000, chain[:-1], -1)
        self.check(100000, chain[:-1] + [[0, 2]], 1)


if __name__ == '__main__':
    unittest.main()
