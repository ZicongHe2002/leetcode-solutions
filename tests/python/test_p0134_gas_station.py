import unittest
from itertools import product

from python.p0134_gas_station import Solution


def possible_starts_by_simulation(gas, cost):
    valid = []
    for start in range(len(gas)):
        tank = 0
        for step in range(len(gas)):
            station = (start + step) % len(gas)
            tank += gas[station] - cost[station]
            if tank < 0:
                break
        else:
            valid.append(start)
    return valid


class GasStationTests(unittest.TestCase):
    def check(self, gas, cost, expected=None):
        before_gas, before_cost = gas[:], cost[:]
        result = Solution().canCompleteCircuit(gas, cost)
        self.assertIs(type(result), int)
        if expected is None:
            valid = possible_starts_by_simulation(gas, cost)
            if valid:
                self.assertIn(result, valid)
            else:
                self.assertEqual(result, -1)
        else:
            self.assertEqual(result, expected)
        self.assertEqual(gas, before_gas)
        self.assertEqual(cost, before_cost)

    def test_all_small_supply_cost_arrays_including_multiple_start_extensions(self):
        checks = 0
        for size in range(1, 5):
            for supply in product(range(3), repeat=size):
                for expense in product(range(3), repeat=size):
                    self.check(list(supply), list(expense))
                    checks += 1
        self.assertEqual(checks, 7380)

    def test_maximum_lengths_unique_last_start_deficit_and_single_station(self):
        gas = [0] * 99999 + [10000]
        cost = [1] * 9999 + [0] * 90001
        cost[-2] = 1
        self.check(gas, cost, 99999)
        self.check([0] * 100000, [10000] * 100000, -1)
        self.check([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3)
        self.check([0], [0], 0)
        self.check([0], [10000], -1)
        self.check([10000], [0], 0)


if __name__ == '__main__':
    unittest.main()
