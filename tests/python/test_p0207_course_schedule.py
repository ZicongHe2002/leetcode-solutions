import unittest
from itertools import permutations

from python.p0207_course_schedule import Solution


def order_oracle(courses, prerequisites):
    for order in permutations(range(courses)):
        positions = {course: index for index, course in enumerate(order)}
        if all(positions[prerequisite] < positions[course] for course, prerequisite in prerequisites):
            return True
    return False


class CourseTests(unittest.TestCase):
    def check(self, courses, prerequisites, expected):
        before, pairs = [pair[:] for pair in prerequisites], prerequisites[:]
        self.assertIs(Solution().canFinish(courses, prerequisites), expected)
        self.assertEqual(prerequisites, before)
        for actual, original in zip(prerequisites, pairs):
            self.assertIs(actual, original)

    def test_all_small_graphs_against_permutation_oracle(self):
        checks = 0
        for courses in range(1, 5):
            possible = [(a, b) for a in range(courses) for b in range(courses)
                        if courses < 4 or a != b]
            for mask in range(1 << len(possible)):
                prerequisites = [list(pair) for i, pair in enumerate(possible) if mask & (1 << i)]
                self.check(courses, prerequisites, order_oracle(courses, prerequisites))
                checks += 1
        self.assertEqual(checks, 4626)

    def test_cycles_isolated_courses_and_maximum_contract(self):
        for courses, prerequisites, expected in [
                (2, [[1, 0]], True), (2, [[1, 0], [0, 1]], False),
                (3, [[1, 1]], False), (4, [[2, 1]], True),
                (2, [[1, 0], [1, 0]], True), (0, [], True)]:
            self.check(courses, prerequisites, expected)
        chain = [[course, course - 1] for course in range(1, 2000)]
        self.check(2000, chain, True)
        self.check(2000, chain + [[0, 1999]], False)
        dag = []
        for distance in range(1, 4):
            for course in range(distance, 2000):
                dag.append([course, course - distance])
                if len(dag) == 5000:
                    break
            if len(dag) == 5000:
                break
        self.assertEqual(len(dag), 5000)
        self.check(2000, dag, True)


if __name__ == '__main__':
    unittest.main()
