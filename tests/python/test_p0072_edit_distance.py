import unittest
from collections import deque
from itertools import product

from python.p0072_edit_distance import Solution


def shortest_edit_graph(source, target):
    limit = max(len(source), len(target))
    visited, pending = {source}, deque([(source, 0)])
    while pending:
        word, distance = pending.popleft()
        if word == target:
            return distance
        candidates = set()
        for index in range(len(word)):
            candidates.add(word[:index] + word[index + 1:])
            for character in 'ab':
                candidates.add(word[:index] + character + word[index + 1:])
        if len(word) < limit:
            for index in range(len(word) + 1):
                for character in 'ab':
                    candidates.add(word[:index] + character + word[index:])
        for candidate in candidates - visited:
            visited.add(candidate)
            pending.append((candidate, distance + 1))


class EditDistanceTests(unittest.TestCase):
    def check(self, left, right, expected):
        result = Solution().minDistance(left, right)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_binary_words_against_shortest_edit_graph(self):
        words = [''.join(chars) for size in range(5) for chars in product('ab', repeat=size)]
        checks = 0
        for left in words:
            for right in words:
                self.check(left, right, shortest_edit_graph(left, right))
                checks += 1
        self.assertEqual(checks, 961)

    def test_maximum_lengths_empty_substitution_and_shift_boundaries(self):
        self.check('a' * 500, 'b' * 500, 500)
        self.check('a' * 500, 'a' * 500, 0)
        self.check('', 'a' * 500, 500)
        self.check('ab' * 250, 'ba' * 250, 2)
        self.check('horse', 'ros', 3)


if __name__ == '__main__':
    unittest.main()
