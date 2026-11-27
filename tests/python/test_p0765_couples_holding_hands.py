import unittest
from collections import deque
from itertools import combinations, permutations

from python.p0765_couples_holding_hands import Solution


def actual_arbitrary_swap_distances(size):
    distance = {state: 0 for state in permutations(range(size))
                if all(state[index] ^ 1 == state[index + 1] for index in range(0, size, 2))}
    frontier = deque(distance)
    swaps = list(combinations(range(size), 2))
    while frontier:
        state = frontier.popleft()
        for left, right in swaps:
            changed = list(state)
            changed[left], changed[right] = changed[right], changed[left]
            moved = tuple(changed)
            if moved not in distance:
                distance[moved] = distance[state] + 1
                frontier.append(moved)
    return distance


class CouplesHandsTests(unittest.TestCase):
    def check(self, row, expected):
        before = row[:]
        result = Solution().minSwapsCouples(row)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, row)
        self.assertEqual(row, before)

    def test_all_two_three_four_couple_permutations_against_actual_swap_bfs(self):
        checked = 0
        for couples in range(2, 5):
            distance = actual_arbitrary_swap_distances(2 * couples)
            for state in permutations(range(2 * couples)):
                self.check(list(state), distance[state])
                checked += 1
        self.assertEqual(checked, 41064)

    def test_official_examples_maximum_identity_and_one_large_couple_cycle(self):
        self.check([0,2,1,3], 1)
        self.check([3,2,0,1], 0)
        self.check(list(range(60)), 0)
        cycle = [person for couple in range(30) for person in (2 * couple + 1, (2 * couple + 2) % 60)]
        self.check(cycle, 29)
        self.check(cycle[::-1], 29)


if __name__ == '__main__':
    unittest.main()
