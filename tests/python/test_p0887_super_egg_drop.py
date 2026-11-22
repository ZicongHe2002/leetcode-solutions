from math import comb
import unittest

from python.p0887_super_egg_drop import Solution


def direct_drop_floor_table(max_eggs, max_floors):
    cost = [[0] * (max_floors + 1) for _ in range(max_eggs + 1)]
    for floors in range(1, max_floors + 1):
        cost[1][floors] = floors
    for eggs in range(2, max_eggs + 1):
        for floors in range(1, max_floors + 1):
            cost[eggs][floors] = 1 + min(
                max(cost[eggs - 1][dropped - 1], cost[eggs][floors - dropped])
                for dropped in range(1, floors + 1))
    return cost


def binomial_coverage(eggs, moves):
    return sum(comb(moves, broken) for broken in range(1, min(eggs, moves) + 1))


class EggDropDirectFloorOracleTests(unittest.TestCase):
    def test_small_egg_floor_states_against_all_drop_floors(self):
        cost = direct_drop_floor_table(6, 30)
        checked = 0
        for eggs in range(1, 7):
            for floors in range(1, 31):
                result = Solution().superEggDrop(eggs, floors)
                self.assertIs(type(result), int)
                self.assertEqual(result, cost[eggs][floors])
                checked += 1
        self.assertEqual(checked, 180)

    def test_maximum_floor_egg_limits_and_binomial_minimality(self):
        solution = Solution()
        for eggs, floors, expected in ((1, 10000, 10000), (2, 10000, 141),
                                       (3, 10000, 40), (100, 10000, 14),
                                       (100, 1, 1), (100, 2, 2), (1, 1, 1)):
            result = solution.superEggDrop(eggs, floors)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected)
            self.assertGreaterEqual(binomial_coverage(eggs, result), floors)
            self.assertLess(binomial_coverage(eggs, result - 1), floors)


if __name__ == '__main__':
    unittest.main()
