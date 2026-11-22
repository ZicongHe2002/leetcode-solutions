import unittest
from heapq import heappop, heappush

from python.p0752_open_the_lock import Solution


def numeric_dijkstra(deadends, target):
    blocked = {int(state) for state in deadends}
    if 0 in blocked:
        return -1
    target = int(target)
    distance = {0: 0}
    pending = [(0, 0)]
    while pending:
        cost, state = heappop(pending)
        if cost != distance[state]:
            continue
        if state == target:
            return cost
        for place in (1, 10, 100, 1000):
            digit = state // place % 10
            for shift in (1 if digit < 9 else -9, -1 if digit else 9):
                following = state + shift * place
                if following not in blocked and cost + 1 < distance.get(following, 100000):
                    distance[following] = cost + 1
                    heappush(pending, (cost + 1, following))
    return -1


class LockTests(unittest.TestCase):
    def check(self, deadends, target, expected=None):
        self.assertTrue(1 <= len(deadends) <= 500)
        self.assertNotIn(target, deadends)
        before = deadends[:]
        if expected is None:
            expected = numeric_dijkstra(deadends, target)
        result = Solution().openLock(deadends, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(deadends, before)

    def test_all_two_wheel_targets_against_independent_cyclic_distances(self):
        for first in range(10):
            for second in range(10):
                self.check(['9999'], f'00{first}{second}', min(first, 10 - first) + min(second, 10 - second))

    def test_numeric_shortest_paths_dead_start_surrounded_target_and_maximum_deadends(self):
        fixtures = [
            (['0201', '0101', '0102', '1212', '2002'], '0202'),
            (['8888'], '0009'),
            (['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'], '8888'),
            (['0000'], '8888'),
            (['0001'], '0000'),
            ([f'{state:04d}' for state in range(1, 501)], '5555'),
        ]
        for deadends, target in fixtures:
            self.check(deadends, target)
        self.assertEqual(numeric_dijkstra(fixtures[-1][0], '5555'), 20)


if __name__ == '__main__':
    unittest.main()
