import unittest
from itertools import product

from python.p0746_min_cost_climbing_stairs import Solution


def enumerate_paid_routes(cost):
    stack, totals = [(0, 0), (1, 0)], []
    while stack:
        position, paid = stack.pop()
        if position == len(cost):
            totals.append(paid)
        elif position < len(cost):
            stack.extend((position + jump, paid + cost[position]) for jump in (1, 2))
    return min(totals)


class MinCostStairsTests(unittest.TestCase):
    def check(self, cost, expected=None):
        before = cost[:]
        result = Solution().minCostClimbingStairs(cost)
        self.assertIs(type(result), int)
        self.assertEqual(result, enumerate_paid_routes(cost) if expected is None else expected, cost[:30])
        self.assertEqual(cost, before)

    def test_every_small_ternary_cost_array_against_actual_paid_routes(self):
        checked = 0
        for size in range(2, 9):
            for values in product((0, 1, 4), repeat=size):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 9837)

    def test_examples_and_thousand_step_maximum_or_free_closed_forms(self):
        self.check([10,15,20], 15)
        self.check([1,100,1,1,1,100,1,1,100,1], 6)
        self.check([999] * 1000, 499500)
        self.check([0] * 1000, 0)
        self.check([0,999] * 500, 0)
        self.check([999,0] * 500, 0)
        self.check([0,999], 0)


if __name__ == '__main__':
    unittest.main()
