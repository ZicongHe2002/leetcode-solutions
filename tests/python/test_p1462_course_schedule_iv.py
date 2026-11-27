import unittest
from itertools import permutations

from python.p1462_course_schedule_iv import Solution


def answer_by_individual_search(size, prerequisites, queries):
    outgoing = [[] for _ in range(size)]
    for first, second in prerequisites:
        outgoing[first].append(second)
    answers = []
    for first, target in queries:
        seen, pending = {first}, [first]
        found = False
        while pending and not found:
            node = pending.pop()
            for following in outgoing[node]:
                if following == target:
                    found = True
                    break
                if following not in seen:
                    seen.add(following)
                    pending.append(following)
        answers.append(found)
    return answers


class PrerequisiteQueryTests(unittest.TestCase):
    def check(self, size, prerequisites, queries, expected=None):
        before_edges = [edge[:] for edge in prerequisites]
        before_queries = [query[:] for query in queries]
        if expected is None:
            expected = answer_by_individual_search(size, prerequisites, queries)
        result = Solution().checkIfPrerequisite(size, prerequisites, queries)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is bool for value in result))
        self.assertEqual(result, expected)
        self.assertEqual(prerequisites, before_edges)
        self.assertEqual(queries, before_queries)

    def test_all_small_ordered_dags_and_distinct_query_pairs(self):
        graphs = checks = 0
        for size in range(2, 6):
            possible = [(first, second) for first in range(size) for second in range(first + 1, size)]
            queries = [list(pair) for pair in permutations(range(size), 2)]
            for mask in range(1 << len(possible)):
                edges = [list(edge) for index, edge in enumerate(possible) if mask >> index & 1]
                self.check(size, edges, queries)
                graphs += 1
                checks += len(queries)
        self.assertEqual((graphs, checks), (1098, 21300))

    def test_maximum_courses_queries_reverse_numbering_chain_and_dense_dag(self):
        queries = [list(pair) for pair in permutations(range(100), 2)]
        queries += [query[:] for query in queries[:100]]
        self.assertEqual(len(queries), 10000)
        expected = [first > second for first, second in queries]
        self.check(100, [[course, course - 1] for course in range(1, 100)], queries, expected)
        dense = [[first, second] for first in range(100) for second in range(first)]
        self.assertEqual(len(dense), 4950)
        self.check(100, dense, queries, expected)


if __name__ == '__main__':
    unittest.main()
