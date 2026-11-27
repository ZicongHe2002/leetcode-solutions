import unittest
from itertools import combinations, product

from python.p0737_sentence_similarity_ii import Solution


def graph_reachability(left, right, pairs):
    if len(left) != len(right):
        return False
    graph = {}
    for a, b in pairs:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    for start, target in zip(left, right):
        seen, stack = {start}, [start]
        while stack:
            current = stack.pop()
            for neighbor in graph.get(current, []):
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        if target not in seen:
            return False
    return True


class SentenceSimilarityTwoTests(unittest.TestCase):
    def check(self, left, right, pairs, expected=None):
        before = (left[:], right[:], [pair[:] for pair in pairs])
        result = Solution().areSentencesSimilarTwo(left, right, pairs)
        self.assertIs(type(result), bool)
        self.assertEqual(result, graph_reachability(left, right, pairs) if expected is None else expected)
        self.assertEqual((left, right, pairs), before)

    def test_all_small_relations_and_sentence_pairs_against_direct_graph_search(self):
        edges = list(combinations('abc', 2))
        sentences = [list(chars) for size in range(1, 4) for chars in product('abc', repeat=size)]
        checked = 0
        for mask in range(8):
            pairs = [list(edge) for index, edge in enumerate(edges) if mask >> index & 1]
            for left, right in product(sentences, repeat=2):
                self.check(left, right, pairs)
                checked += 1
        self.assertEqual(checked, 12168)

    def test_multihop_unknown_words_case_duplicates_and_maximum_chain(self):
        self.check(['great','acting','skills'], ['fine','drama','talent'],
                   [['great','good'],['fine','good'],['drama','acting'],['skills','talent']], True)
        self.check(['I','love','leetcode'], ['I','love','onepiece'],
                   [['manga','onepiece'],['platform','anime'],['leetcode','platform'],['anime','manga']], True)
        self.check(['a'], ['c'], [['a','b'],['b','c']], True)
        self.check(['new'], ['new'], [], True)
        self.check(['new'], ['other'], [], False)
        self.check(['Word'], ['word'], [], False)
        self.check(['a'], ['b'], [['a','b'],['b','a'],['a','b']], True)
        words = ['a' * 17 + ''.join(chr(97 + digit) for digit in (i // 676, i // 26 % 26, i % 26)) for i in range(2001)]
        pairs = [[left, right] for left, right in zip(words, words[1:])]
        self.assertEqual((len(pairs), {len(word) for word in words}), (2000, {20}))
        self.check([words[0]] * 1000, [words[-1]] * 1000, pairs, True)
        self.check([words[0]] * 1000, [words[-1]] * 999 + ['z' * 20], pairs, False)


if __name__ == '__main__':
    unittest.main()
