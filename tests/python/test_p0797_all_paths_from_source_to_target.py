from itertools import permutations
import unittest

from python.p0797_all_paths_from_source_to_target import Solution


def candidate_vertex_permutations(graph):
    paths = set()
    for length in range(len(graph) - 1):
        for middle in permutations(range(1, len(graph) - 1), length):
            path = (0,) + middle + (len(graph) - 1,)
            if all(right in graph[left] for left, right in zip(path, path[1:])):
                paths.add(path)
    return paths


def ordered_middle_subsets(graph):
    paths = set()
    for mask in range(1 << (len(graph) - 2)):
        path = (0,) + tuple(node for node in range(1, len(graph) - 1)
                            if mask >> (node - 1) & 1) + (len(graph) - 1,)
        if all(right in graph[left] for left, right in zip(path, path[1:])):
            paths.add(path)
    return paths


class CompleteDagPathEnumerationTests(unittest.TestCase):
    def check(self, graph, expected=None):
        before = [neighbors[:] for neighbors in graph]
        if expected is None:
            expected = candidate_vertex_permutations(graph)
        result = Solution().allPathsSourceTarget(graph)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(path) is list for path in result))
        actual = {tuple(path) for path in result}
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(result))
        self.assertEqual(len({id(path) for path in result}), len(result))
        self.assertEqual(graph, before)
        return result

    def test_all_small_ordered_dags_and_non_topological_numeric_labels(self):
        checks = 0
        for size in range(2, 6):
            possible = [(left, right) for left in range(size) for right in range(left + 1, size)]
            for mask in range(1 << len(possible)):
                graph = [[] for _ in range(size)]
                for index, (left, right) in enumerate(possible):
                    if mask >> index & 1:
                        graph[left].append(right)
                self.check(graph)
                checks += 1
        self.assertEqual(checks, 1098)
        labels = [0, 3, 1, 2, 4]
        graph = [[] for _ in labels]
        for left in range(5):
            for right in range(left + 1, 5):
                graph[labels[left]].append(labels[right])
        self.check(graph)

    def test_maximum_dag_output_long_chain_and_unreachable_target(self):
        complete = [list(range(node + 1, 15)) for node in range(15)]
        result = self.check(complete, ordered_middle_subsets(complete))
        self.assertEqual(len(result), 8192)
        chain = [[node + 1] for node in range(14)] + [[]]
        self.check(chain, ordered_middle_subsets(chain))
        unreachable = [list(range(node + 1, 14)) for node in range(14)] + [[]]
        self.check(unreachable, set())
        self.check([[3, 2, 1], [3], [3], []])


if __name__ == '__main__':
    unittest.main()
