from collections import Counter
from itertools import product
import unittest

from python.p0332_reconstruct_itinerary import Solution


def all_ticket_order_minimum(tickets):
    best = None

    def visit(airport, used, route):
        nonlocal best
        if len(route) == len(tickets) + 1:
            candidate = tuple(route)
            if best is None or candidate < best:
                best = candidate
            return
        for index, (origin, destination) in enumerate(tickets):
            if origin == airport and not used & (1 << index):
                visit(destination, used | (1 << index), route + [destination])

    visit('JFK', 0, ['JFK'])
    return None if best is None else list(best)


class ItineraryTicketIndexOracleTests(unittest.TestCase):
    def check(self, tickets, expected=None):
        before = [row[:] for row in tickets]
        if expected is None:
            expected = all_ticket_order_minimum(tickets)
        self.assertIsNotNone(expected)
        result = Solution().findItinerary(tickets)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(airport) is str for airport in result))
        self.assertEqual(result, expected)
        self.assertEqual(len(result), len(tickets) + 1)
        self.assertEqual(Counter(zip(result, result[1:])), Counter(map(tuple, tickets)))
        self.assertEqual(tickets, before)

    def test_all_short_valid_walk_ticket_multisets_and_input_orders(self):
        walks = checks = 0
        for length in range(1, 7):
            for destinations in product(('JFK', 'KUL', 'NRT'), repeat=length):
                route = ('JFK',) + destinations
                if any(origin == destination for origin, destination in zip(route, route[1:])):
                    continue
                tickets = [list(edge) for edge in zip(route, route[1:])]
                self.check(tickets)
                self.check(list(reversed(tickets)))
                walks += 1
                checks += 2
        self.assertEqual((walks, checks), (126, 252))

    def test_maximum_tickets_duplicate_edges_and_lexical_dead_end(self):
        tickets = [['JFK', 'AAA'], ['AAA', 'JFK']] * 150
        self.check(list(reversed(tickets)), ['JFK'] + ['AAA', 'JFK'] * 150)
        tickets = []
        for destination in ('AAB', 'AAA'):
            tickets += [['JFK', destination], [destination, 'JFK']] * 75
        self.assertEqual(len(tickets), 300)
        self.check(tickets, ['JFK'] + ['AAA', 'JFK'] * 75 + ['AAB', 'JFK'] * 75)
        self.check([['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']],
                   ['JFK', 'NRT', 'JFK', 'KUL'])


if __name__ == '__main__':
    unittest.main()
