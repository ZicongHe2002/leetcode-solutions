from collections import deque
from itertools import product
import unittest

from python.p0126_word_ladder_ii import Solution


def explicit_path_queue_oracle(begin, end, words):
    if begin == end:
        return [[begin]]
    if end not in words:
        return []
    nodes = set(words) | {begin}
    graph = {word: [other for other in nodes if sum(a != b for a, b in zip(word, other)) == 1]
             for word in nodes}
    pending = deque([[begin]])
    answers = []
    while pending:
        path = pending.popleft()
        if answers and len(path) > len(answers[0]):
            break
        if path[-1] == end:
            answers.append(path)
            continue
        for neighbor in graph[path[-1]]:
            if neighbor not in path:
                pending.append(path + [neighbor])
    return answers


class ShortestLadderDagTests(unittest.TestCase):
    def check(self, begin, end, words, expected=None):
        before = words[:]
        result = Solution().findLadders(begin, end, words)
        normalized = sorted(map(tuple, result))
        expected = explicit_path_queue_oracle(begin, end, words) if expected is None else expected
        self.assertEqual(normalized, sorted(map(tuple, expected)))
        self.assertEqual(len(normalized), len(set(normalized)))
        self.assertEqual(words, before)

    def test_all_small_dictionary_subsets_and_distinct_endpoint_pairs(self):
        vocabulary = [''.join(chars) for chars in product('ab', repeat=3)]
        queries = 0
        for mask in range(1 << len(vocabulary)):
            words = [word for bit, word in enumerate(vocabulary) if mask & (1 << bit)]
            for begin in vocabulary:
                for end in vocabulary:
                    if begin != end:
                        self.check(begin, end, words)
                        queries += 1
        self.assertEqual(queries, 14336)

    def test_multiple_same_layer_parents_missing_end_and_dictionary_limit(self):
        words = [''.join(chars) for chars in product('ab', repeat=3)]
        paths = Solution().findLadders('aaa', 'bbb', words)
        self.assertEqual(len(paths), 6)
        self.check('aaa', 'bbb', words)
        self.check('aaa', 'bbb', ['aab', 'abb'], [])
        large = [''.join(chars) for chars in product('abcd', repeat=5)][:500]
        self.assertEqual(len(large), 500)
        self.check('aaaaa', 'baaaa', large, [['aaaaa', 'baaaa']])
        disconnected = large[:499] + ['zzzzz']
        self.check('aaaaa', 'zzzzz', disconnected, [])
        self.check('aaa', 'aaa', [], [['aaa']])


if __name__ == '__main__':
    unittest.main()
