from collections import deque
import unittest

from python.p0365_water_and_jug_problem import Solution


def jug_state_bfs(x, y, target):
    queue = deque([(0, 0)])
    seen = {(0, 0)}
    while queue:
        first, second = queue.popleft()
        if target in (first, second, first + second):
            return True
        to_second = min(first, y - second)
        to_first = min(second, x - first)
        neighbors = [(x, second), (first, y), (0, second), (first, 0),
                     (first - to_second, second + to_second),
                     (first + to_first, second - to_first)]
        for state in neighbors:
            if state not in seen:
                seen.add(state)
                queue.append(state)
    return False


class JugGcdReachabilityTests(unittest.TestCase):
    def test_all_small_capacities_and_targets_against_physical_states(self):
        queries = 0
        for x in range(9):
            for y in range(9):
                for target in range(x + y + 3):
                    actual = Solution().canMeasureWater(x, y, target)
                    self.assertIs(type(actual), bool)
                    self.assertEqual(actual, jug_state_bfs(x, y, target))
                    queries += 1
        self.assertEqual(queries, 891)

    def test_maximum_capacities_gcd_and_combined_water(self):
        for x, y, target, expected in [(3, 5, 4, True), (3, 5, 8, True),
                                       (2, 6, 5, False), (1, 1, 3, False),
                                       (999999, 1000000, 1, True),
                                       (1000000, 1000000, 999999, False),
                                       (500000, 1000000, 500000, True),
                                       (0, 0, 0, True), (0, 0, 1, False)]:
            self.assertEqual(Solution().canMeasureWater(x, y, target), expected)


if __name__ == '__main__':
    unittest.main()
