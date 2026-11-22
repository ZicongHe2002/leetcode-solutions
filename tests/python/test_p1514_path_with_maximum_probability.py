from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations, product
import unittest

from python.p1514_path_with_maximum_probability import Solution


def all_simple_fraction_paths(n, edges, probabilities, start, end):
    neighbors = [[] for _ in range(n)]
    for (left, right), probability in zip(edges, probabilities):
        neighbors[left].append((right, probability))
        neighbors[right].append((left, probability))
    best = Fraction(0)

    def extend(node, used, probability):
        nonlocal best
        if node == end:
            best = max(best, probability)
            return
        for target, chance in neighbors[node]:
            if target not in used:
                extend(target, used | {target}, probability * chance)

    extend(start, {start}, Fraction(1))
    return best


class MultiplicativeProbabilityPathTests(unittest.TestCase):
    def check(self, n, edges, probabilities, start, end, expected=None):
        before_edges = [edge[:] for edge in edges]
        input_probabilities = [float(probability) for probability in probabilities]
        before_probabilities = input_probabilities[:]
        if expected is None:
            expected = all_simple_fraction_paths(n, edges, probabilities, start, end)
        result = Solution().maxProbability(n, edges, input_probabilities, start, end)
        self.assertIs(type(result), float)
        self.assertLessEqual(abs(result - float(expected)), 1e-10)
        self.assertEqual(edges, before_edges)
        self.assertEqual(input_probabilities, before_probabilities)

    def test_all_small_graphs_probabilities_and_distinct_endpoint_pairs(self):
        graphs = checks = 0
        options = (None, Fraction(0), Fraction(1, 2), Fraction(1))
        for n in range(2, 5):
            possible = list(combinations(range(n), 2))
            for values in product(options, repeat=len(possible)):
                edges, probabilities = [], []
                for pair, chance in zip(possible, values):
                    if chance is not None:
                        edges.append(list(pair))
                        probabilities.append(chance)
                for start in range(n):
                    for end in range(n):
                        if start != end:
                            self.check(n, edges, probabilities, start, end)
                            checks += 1
                graphs += 1
        self.assertEqual((graphs, checks), (4164, 49544))

    def test_maximum_nodes_edges_zero_one_and_nonbinary_long_products(self):
        n = 10000
        chain = [[node, node + 1] for node in range(n - 1)]
        self.check(n, chain, [Fraction(1)] * (n - 1), 0, n - 1, 1)
        with localcontext() as context:
            context.prec = 50
            expected = Decimal('0.9999') ** (n - 1)
        self.check(n, chain, [Fraction(9999, 10000)] * (n - 1), 0, n - 1, expected)
        self.check(n, chain, [Fraction(0)] * (n - 1), 0, n - 1, 0)
        self.check(n, chain[:-1], [Fraction(1)] * (n - 2), 0, n - 1, 0)
        dense = chain + [[n - 1, 0]] + [[node, (node + 2) % n] for node in range(n)]
        self.assertEqual(len(dense), 20000)
        self.check(n, dense, [Fraction(1, 2)] * len(dense), 0, n - 1, Fraction(1, 2))


if __name__ == '__main__':
    unittest.main()
