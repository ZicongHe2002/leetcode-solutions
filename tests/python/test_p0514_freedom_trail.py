from collections import deque
from itertools import product
import unittest

from python.p0514_freedom_trail import Solution


def unit_action_bfs(ring, key):
    queue = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while queue:
        position, matched, steps = queue.popleft()
        if matched == len(key):
            return steps
        following = [((position - 1) % len(ring), matched), ((position + 1) % len(ring), matched)]
        if ring[position] == key[matched]:
            following.append((position, matched + 1))
        for state in following:
            if state not in seen:
                seen.add(state)
                queue.append((*state, steps + 1))
    raise AssertionError('the key must be spellable')


class CircularPositionCostTests(unittest.TestCase):
    def check(self, ring, key, expected=None):
        actual = Solution().findRotateSteps(ring, key)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, unit_action_bfs(ring, key) if expected is None else expected)

    def test_all_small_binary_rings_and_spellable_keys_against_unit_actions(self):
        queries = 0
        for size in range(1, 6):
            for chars in product('ab', repeat=size):
                ring = ''.join(chars)
                alphabet = ''.join(sorted(set(ring)))
                for length in range(6):
                    for key in product(alphabet, repeat=length):
                        self.check(ring, ''.join(key))
                        queries += 1
        self.assertEqual(queries, 3336)

    def test_maximum_lengths_press_counts_reverse_shortcut_and_multiple_positions(self):
        self.check('a' * 100, 'a' * 100, 100)
        self.check('a' * 99 + 'b', 'b' * 100, 101)
        self.check('ab' * 50, 'ba' * 50, 200)
        self.check('godding', 'gd', 4)
        self.check('ababc', 'cba')
        self.check('ababc', 'abbca')
        self.check('a', '', 0)


if __name__ == '__main__':
    unittest.main()
