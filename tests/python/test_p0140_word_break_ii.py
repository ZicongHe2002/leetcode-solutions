import unittest
from itertools import product

from python.p0140_word_break_ii import Solution


def cut_mask_oracle(text, words):
    if not text:
        return []
    allowed = set(words)
    answers = []
    for mask in range(1 << (len(text) - 1)):
        pieces = []
        start = 0
        for boundary in range(1, len(text)):
            if mask & (1 << (boundary - 1)):
                pieces.append(text[start:boundary])
                start = boundary
        pieces.append(text[start:])
        if all(piece in allowed for piece in pieces):
            answers.append(' '.join(pieces))
    return sorted(answers)


class WordBreakSentencesTests(unittest.TestCase):
    def check(self, text, words, expected=None):
        before = words[:]
        actual = Solution().wordBreak(text, words)
        self.assertEqual(words, before)
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(sorted(actual), cut_mask_oracle(text, words)
                         if expected is None else sorted(expected))
        return actual

    def test_all_small_texts_and_dictionary_subsets(self):
        vocabulary = ['a', 'b', 'aa', 'ab', 'ba', 'bb']
        queries = 0
        for mask in range(1 << len(vocabulary)):
            words = [word for index, word in enumerate(vocabulary) if mask & (1 << index)]
            for size in range(7):
                for chars in product('ab', repeat=size):
                    self.check(''.join(chars), words)
                    queries += 1
        self.assertEqual(queries, 8128)

    def test_examples_output_growth_and_contract_boundaries(self):
        self.check('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog'],
                   ['cats and dog', 'cat sand dog'])
        self.check('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple'],
                   ['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple'])
        self.check('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'], [])
        self.assertEqual(len(self.check('a' * 12, ['a', 'aa', 'aaa'])), 927)
        self.check('a' * 20, ['a'], [' '.join('a' * 20)])
        self.check('a' * 20, ['a' * 10], ['a' * 10 + ' ' + 'a' * 10])
        words = [''.join(chars) for size in range(1, 10)
                 for chars in product('ab', repeat=size)][:999] + ['z' * 10]
        self.assertEqual(len(words), 1000)
        self.check('z' * 20, words, ['z' * 10 + ' ' + 'z' * 10])
        self.check('a', [], [])
        self.check('', ['a'], [])


if __name__ == '__main__':
    unittest.main()
