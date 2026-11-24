import unittest
from itertools import combinations

from python.p0547_number_of_provinces import Solution


def matrix(size, edges):
    result = [[int(row == column) for column in range(size)] for row in range(size)]
    for left, right in edges:
        result[left][right] = result[right][left] = 1
    return result


def transitive_components(original):
    reachable = [row[:] for row in original]
    for middle in range(len(reachable)):
        for start in range(len(reachable)):
            if reachable[start][middle]:
                for end in range(len(reachable)):
                    reachable[start][end] |= reachable[middle][end]
    return len({tuple(row) for row in reachable})


class ProvinceTests(unittest.TestCase):
    def check(self, graph):
        before = [row[:] for row in graph]
        identities = [id(row) for row in graph]
        result = Solution().findCircleNum(graph)
        self.assertIs(type(result), int)
        self.assertEqual(result, transitive_components(before))
        self.assertEqual(graph, before)
        self.assertEqual([id(row) for row in graph], identities)

    def test_all_small_symmetric_matrices_against_boolean_transitive_closure(self):
        checks = 0
        for size in range(1, 6):
            possible_edges = list(combinations(range(size), 2))
            for mask in range(1 << len(possible_edges)):
                edges = [edge for bit, edge in enumerate(possible_edges) if mask & (1 << bit)]
                self.check(matrix(size, edges))
                checks += 1
        self.assertEqual(checks, 1099)

    def test_maximum_isolated_complete_chain_clusters_and_empty_extension(self):
        self.check(matrix(200, []))
        self.check(matrix(200, combinations(range(200), 2)))
        self.check(matrix(200, [(city, city + 1) for city in range(199)]))
        self.check(matrix(200, [(city, city + 1) for city in range(199) if (city + 1) % 50]))
        self.check([])


if __name__ == '__main__':
    unittest.main()
