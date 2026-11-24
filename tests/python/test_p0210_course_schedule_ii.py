import unittest
from itertools import permutations

from python.p0210_course_schedule_ii import Solution


class CourseOrderTests(unittest.TestCase):
    def check(self, size, prerequisites, possible):
        before = [edge[:] for edge in prerequisites]
        result = Solution().findOrder(size, prerequisites)
        if possible:
            self.assertEqual(sorted(result), list(range(size)))
            positions = {course: index for index, course in enumerate(result)}
            self.assertTrue(all(positions[prerequisite] < positions[course] for course, prerequisite in prerequisites))
        else:
            self.assertEqual(result, [])
        self.assertEqual(prerequisites, before)

    def test_all_small_directed_graphs_against_permutation_existence(self):
        checks = 0
        for size in range(1, 5):
            possible_edges = [(course, prerequisite) for course in range(size) for prerequisite in range(size) if course != prerequisite]
            candidates = [(order, {course: index for index, course in enumerate(order)}) for order in permutations(range(size))]
            for mask in range(1 << len(possible_edges)):
                edges = [list(edge) for bit, edge in enumerate(possible_edges) if mask & (1 << bit)]
                possible = any(all(positions[p] < positions[c] for c, p in edges) for _, positions in candidates)
                self.check(size, edges, possible)
                checks += 1
        self.assertEqual(checks, 4165)

    def test_maximum_chain_cycle_isolated_and_self_prerequisite(self):
        edges = [[course, course - 1] for course in range(1, 2000)]
        self.check(2000, edges, True)
        self.check(2000, edges + [[0, 1999]], False)
        self.check(2000, [], True)
        self.check(1, [[0, 0]], False)
        self.check(0, [], True)


if __name__ == '__main__':
    unittest.main()
