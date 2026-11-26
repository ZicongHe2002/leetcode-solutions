from itertools import product
import unittest

from python.p0568_maximum_vacation_days import Solution


def all_itineraries(flights, days):
    best = 0
    for route in product(range(len(flights)), repeat=len(days[0])):
        source, total = 0, 0
        for week, destination in enumerate(route):
            if source != destination and flights[source][destination] == 0:
                break
            total += days[destination][week]
            source = destination
        else:
            best = max(best, total)
    return best


class VacationDaysTests(unittest.TestCase):
    def check(self, flights, days, expected):
        before = ([row[:] for row in flights], [row[:] for row in days])
        result = Solution().maxVacationDays(flights, days)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual((flights, days), before)

    def test_all_small_directed_graphs_and_binary_rewards_against_routes(self):
        checks = 0
        for cities in range(1, 4):
            edges = [(i, j) for i in range(cities) for j in range(cities) if i != j]
            for weeks in range(1, 4 if cities < 3 else 3):
                for flags in product((0, 1), repeat=len(edges)):
                    flights = [[0] * cities for _ in range(cities)]
                    for (source, destination), flag in zip(edges, flags):
                        flights[source][destination] = flag
                    for rewards in product((0, 1), repeat=cities * weeks):
                        days = [list(rewards[c * weeks:(c + 1) * weeks]) for c in range(cities)]
                        self.check(flights, days, all_itineraries(flights, days))
                        checks += 1
        self.assertEqual(checks, 4958)

    def test_direction_one_flight_unreachable_cities_and_maximum_dimensions(self):
        chain = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
        self.check(chain, [[0], [0], [7]], 0)
        self.check(chain, [[0, 0], [0, 0], [7, 7]], 7)
        self.check([[0, 1], [0, 0]], [[0], [7]], 7)
        self.check([[0, 0], [1, 0]], [[0], [7]], 0)
        connected = [[int(i != j) for j in range(100)] for i in range(100)]
        days = [[(city + week) % 8 for week in range(100)] for city in range(100)]
        self.check(connected, days, 700)
        self.check([[0] * 100 for _ in range(100)], [[0] * 100] + [[7] * 100 for _ in range(99)], 0)
        self.check([[0, 1, 1], [1, 0, 1], [1, 1, 0]], [[1, 3, 1], [6, 0, 3], [3, 3, 3]], 12)


if __name__ == '__main__':
    unittest.main()
