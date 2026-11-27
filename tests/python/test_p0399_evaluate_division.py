from itertools import combinations, product
import math
import unittest

from python.p0399_evaluate_division import Solution


def latent_values_and_connectivity(equations, latent, queries):
    parents = {name: name for pair in equations for name in pair}

    def root(name):
        while parents[name] != name:
            name = parents[name]
        return name

    for first, second in equations:
        parents[root(first)] = root(second)
    return [latent[first] / latent[second]
            if first in parents and second in parents and root(first) == root(second)
            else -1.0 for first, second in queries]


class DivisionLatentValueOracleTests(unittest.TestCase):
    def check(self, equations, values, queries, expected):
        before = ([row[:] for row in equations], values[:], [row[:] for row in queries])
        result = Solution().calcEquation(equations, values, queries)
        self.assertIs(type(result), list)
        self.assertEqual(len(result), len(expected))
        for actual, wanted in zip(result, expected):
            self.assertIs(type(actual), float)
            self.assertTrue(math.isclose(actual, wanted, rel_tol=1e-9, abs_tol=1e-9))
        self.assertEqual((equations, values, queries), before)

    def test_all_nonempty_small_graphs_against_latent_values_and_unweighted_dsu(self):
        latent = dict(zip('abcd', (1.0, 2.0, 5.0, 10.0)))
        graphs = checks = 0
        for size in range(2, 5):
            names = list('abcd'[:size])
            possible = list(combinations(names, 2))
            queries = [list(pair) for pair in product(names + ['x'], repeat=2)]
            for mask in range(1, 1 << len(possible)):
                equations = [list(pair) for index, pair in enumerate(possible) if mask & (1 << index)]
                values = [latent[first] / latent[second] for first, second in equations]
                expected = latent_values_and_connectivity(equations, latent, queries)
                for start in range(0, len(queries), 20):
                    self.check(equations, values, queries[start:start + 20], expected[start:start + 20])
                graphs += 1
                checks += len(queries)
        self.assertEqual((graphs, checks), (71, 1696))

    def test_maximum_equation_query_counts_and_disconnected_unknown_variables(self):
        equations = [[f'v{index}', f'v{index + 1}'] for index in range(20)]
        queries = [['v0', f'v{index}'] for index in range(18)] + [['v0', 'v20'], ['v20', 'v0']]
        expected = [float(2**index) for index in range(18)] + [float(2**20), 2.0**-20]
        self.assertEqual((len(equations), len(queries)), (20, 20))
        self.check(equations, [2.0] * 20, queries, expected)
        self.check([['a', 'b'], ['c', 'd']], [2.0, 3.0],
                   [['a', 'c'], ['a', 'a'], ['x', 'x'], ['d', 'c']], [-1.0, 1.0, -1.0, 1.0 / 3.0])


if __name__ == '__main__':
    unittest.main()
