from itertools import combinations
import unittest

from python.p1042_flower_planting_with_no_adjacent import Solution


class FourColorDegreeThreeGardensTests(unittest.TestCase):
    def check(self, n, paths):
        before = [pair[:] for pair in paths]
        colors = Solution().gardenNoAdj(n, paths)
        self.assertIs(type(colors), list)
        self.assertEqual(len(colors), n)
        self.assertTrue(all(type(color) is int and 1 <= color <= 4 for color in colors))
        self.assertTrue(all(colors[left - 1] != colors[right - 1] for left, right in paths))
        self.assertEqual(paths, before)

    def test_all_small_simple_graphs_with_degree_at_most_three(self):
        checks = 0
        for n in range(1, 6):
            possible = list(combinations(range(1, n + 1), 2))
            for mask in range(1 << len(possible)):
                paths = [list(pair) for index, pair in enumerate(possible) if mask >> index & 1]
                degrees = [0] * n
                for left, right in paths:
                    degrees[left - 1] += 1
                    degrees[right - 1] += 1
                if max(degrees) <= 3:
                    self.check(n, paths)
                    checks += 1
        self.assertEqual(checks, 843)

    def test_maximum_gardens_all_four_colors_isolates_chain_and_cycle(self):
        n = 10000
        cliques = [[left, right] for start in range(1, n + 1, 4)
                   for left, right in combinations(range(start, start + 4), 2)]
        self.assertEqual(len(cliques), 15000)
        self.check(n, cliques)
        self.check(n, [])
        chain = [[garden, garden + 1] for garden in range(1, n)]
        self.check(n, chain)
        self.check(n, chain + [[n, 1]])


if __name__ == '__main__':
    unittest.main()
