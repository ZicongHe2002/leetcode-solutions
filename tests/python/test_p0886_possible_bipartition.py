from itertools import combinations
import unittest

from python.p0886_possible_bipartition import Solution


def all_two_group_assignments(n, dislikes):
    return any(all(((assignment >> (first - 1)) & 1) != ((assignment >> (second - 1)) & 1)
                   for first, second in dislikes) for assignment in range(1 << n))


class BipartitionAssignmentOracleTests(unittest.TestCase):
    def check(self, n, dislikes, expected=None):
        before = [row[:] for row in dislikes]
        if expected is None:
            expected = all_two_group_assignments(n, dislikes)
        result = Solution().possibleBipartition(n, dislikes)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(dislikes, before)

    def test_all_small_simple_graphs_against_all_group_assignments(self):
        checked = 0
        for n in range(1, 6):
            pairs = list(combinations(range(1, n + 1), 2))
            for mask in range(1 << len(pairs)):
                dislikes = [list(pair) for index, pair in enumerate(pairs) if mask & (1 << index)]
                self.check(n, dislikes)
                checked += 1
        self.assertEqual(checked, 1099)

    def test_maximum_people_edges_and_disconnected_odd_component(self):
        chain = [[person, person + 1] for person in range(1, 2000)]
        self.check(2000, chain, True)
        self.check(2000, chain + [[1, 3]], False)
        dislikes = [[first, second] for first in range(1, 101) for second in range(101, 201)]
        self.assertEqual(len(dislikes), 10000)
        self.check(2000, dislikes, True)
        self.check(2000, [[1998, 1999], [1999, 2000], [1998, 2000]], False)
        self.check(2000, [], True)


if __name__ == '__main__':
    unittest.main()
