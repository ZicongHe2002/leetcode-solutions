import unittest
from itertools import product

from python.p0787_cheapest_flights_within_k_stops import Solution


def all_bounded_walks(length, flights, source, target, stops):
    outgoing = [[] for _ in range(length)]
    for first, second, price in flights:
        outgoing[first].append((second, price))
    best = None

    def walk(node, remaining, total):
        nonlocal best
        if node == target:
            best = total if best is None else min(best, total)
            return
        if remaining:
            for following, price in outgoing[node]:
                walk(following, remaining - 1, total + price)

    walk(source, stops + 1, 0)
    return -1 if best is None else best


class FlightStopTests(unittest.TestCase):
    def check(self, length, flights, source, target, stops, expected=None):
        before = [flight[:] for flight in flights]
        if expected is None:
            expected = all_bounded_walks(length, flights, source, target, stops)
        result = Solution().findCheapestPrice(length, flights, source, target, stops)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(flights, before)

    def test_small_legal_graphs_against_all_bounded_walks(self):
        edges = [(first, second) for first in range(3) for second in range(3) if first != second]
        graphs = checks = 0
        for prices in product((0, 1, 4), repeat=len(edges)):
            flights = [[first, second, price] for (first, second), price in zip(edges, prices) if price]
            if len(flights) > 3:
                continue
            graphs += 1
            for source in range(3):
                for target in range(3):
                    if source != target:
                        for stops in range(3):
                            self.check(3, flights, source, target, stops)
                            checks += 1
        self.assertEqual((graphs, checks), (233, 4194))

    def test_maximum_nodes_edges_and_stop_limited_tradeoffs(self):
        chain = [[index, index + 1, 100] for index in range(99)]
        self.check(100, chain, 0, 99, 98, 9900)
        self.check(100, chain, 0, 99, 97, -1)
        self.check(100, chain + [[0, 99, 10000]], 0, 99, 0, 10000)
        self.check(100, chain + [[0, 99, 10000]], 0, 99, 98, 9900)
        dense = [[first, second, 10000] for first in range(100) for second in range(first + 1, 100)]
        self.assertEqual(len(dense), 4950)
        self.check(100, dense, 0, 99, 99, 10000)
        self.check(100, dense, 99, 0, 99, -1)
        flights = [[0, 1, 1], [1, 2, 1], [0, 2, 5], [2, 3, 1]]
        self.check(4, flights, 0, 3, 1, 6)
        self.check(4, flights, 0, 3, 2, 3)


if __name__ == '__main__':
    unittest.main()
