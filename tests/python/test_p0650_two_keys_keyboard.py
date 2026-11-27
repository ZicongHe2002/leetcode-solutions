import unittest
from collections import deque

from python.p0650_two_keys_keyboard import Solution


def keyboard_distances(limit):
    pending = deque([(1, 0, 0)])
    seen = {(1, 0)}
    answers = {}
    while pending:
        screen, clipboard, distance = pending.popleft()
        answers.setdefault(screen, distance)
        following = [(screen, screen)]
        if clipboard and screen + clipboard <= limit:
            following.append((screen + clipboard, clipboard))
        for state in following:
            if state not in seen:
                seen.add(state)
                pending.append((*state, distance + 1))
    return answers


class TwoKeyKeyboardTests(unittest.TestCase):
    def test_entire_valid_domain_against_actual_copy_paste_bfs(self):
        expected = keyboard_distances(1000)
        self.assertEqual(set(expected), set(range(1, 1001)))
        for target in range(1, 1001):
            actual = Solution().minSteps(target)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, expected[target], target)


if __name__ == '__main__':
    unittest.main()
