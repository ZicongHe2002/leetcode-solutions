import unittest
from itertools import permutations, product

from python.p0127_word_ladder import Solution


def explicit_word_graph_distance(begin, end, words):
    if end not in words:
        return 0
    nodes = sorted(set(words) | {begin})
    distance = [[1000] * len(nodes) for _ in nodes]
    for first, word in enumerate(nodes):
        distance[first][first] = 0
        for second, other in enumerate(nodes):
            if sum(a != b for a, b in zip(word, other)) == 1:
                distance[first][second] = 1
    for middle in range(len(nodes)):
        for first in range(len(nodes)):
            for second in range(len(nodes)):
                distance[first][second] = min(distance[first][second], distance[first][middle] + distance[middle][second])
    result = distance[nodes.index(begin)][nodes.index(end)]
    return result + 1 if result < 1000 else 0


class WordLadderTests(unittest.TestCase):
    def check(self, begin, end, words, expected=None):
        before = words[:]
        if expected is None:
            expected = explicit_word_graph_distance(begin, end, words)
        result = Solution().ladderLength(begin, end, words)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(words, before)

    def test_all_small_nonempty_dictionaries_and_distinct_endpoints(self):
        checks = 0
        for size in (2, 3):
            nodes = [''.join(letters) for letters in product('ab', repeat=size)]
            for mask in range(1, 1 << len(nodes)):
                words = [word for index, word in enumerate(nodes) if mask >> index & 1]
                for begin, end in permutations(nodes, 2):
                    self.check(begin, end, words)
                    checks += 1
        self.assertEqual(checks, 14460)

    def test_maximum_dictionary_word_length_disconnected_component_and_known_path(self):
        words = ['a' * 7 + ''.join(letters) for letters in product('abcdefghijklmnopqrstuvwxyz', repeat=3)][:4999]
        words.append('zzzzzzzzzz')
        self.assertEqual(len(set(words)), 5000)
        self.check('aaaaaaaaaa', 'zzzzzzzzzz', words, 0)
        self.check('aaaaaaaaaa', 'aaaaaaaaab', ['aaaaaaaaab'], 2)
        self.check('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'], 5)
        self.check('hit', 'cog', ['hot', 'dot', 'dog'], 0)


if __name__ == '__main__':
    unittest.main()
