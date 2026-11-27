import random
import unittest
from collections import deque
from itertools import product

from python.p0664_strange_printer import Solution


def overwrite_distances(length):
    blank = ('',) * length
    distance = {blank: 0}
    pending = deque([blank])
    while pending:
        state = pending.popleft()
        for left in range(length):
            for right in range(left + 1, length + 1):
                for char in 'abc':
                    following = state[:left] + (char,) * (right - left) + state[right:]
                    if following not in distance:
                        distance[following] = distance[state] + 1
                        pending.append(following)
    return distance


def endpoint_split_oracle(text):
    size = len(text)
    table = [[0] * size for _ in range(size)]
    for length in range(1, size + 1):
        for left in range(size - length + 1):
            right = left + length - 1
            if left == right:
                table[left][right] = 1
            elif text[left] == text[right]:
                table[left][right] = table[left][right - 1]
            else:
                table[left][right] = min(table[left][cut] + table[cut + 1][right]
                                         for cut in range(left, right))
    return table[0][-1]


class StrangePrinterTests(unittest.TestCase):
    def check(self, text, expected):
        actual = Solution().strangePrinter(text)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected, text)

    def test_all_small_three_letter_targets_against_actual_overwrite_bfs(self):
        checked = 0
        for length in range(1, 7):
            distances = overwrite_distances(length)
            for target in product('abc', repeat=length):
                self.check(''.join(target), distances[target])
                checked += 1
        self.assertEqual(checked, 1092)

    def test_maximum_lengths_known_bounds_and_separate_endpoint_recurrence(self):
        self.check('a' * 100, 1)
        self.check('ab' * 50, 51)
        self.check('a' * 33 + 'b' * 34 + 'a' * 33, 2)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.check(''.join(char * (4 if index < 22 else 3) for index, char in enumerate(alphabet)), 26)
        self.check('a' * 24 + alphabet + alphabet[::-1] + 'a' * 24, 26)
        rng = random.Random(664)
        for _ in range(50):
            text = ''.join(rng.choice('abcd') for _ in range(rng.randint(1, 100)))
            self.check(text, endpoint_split_oracle(text))


if __name__ == '__main__':
    unittest.main()
