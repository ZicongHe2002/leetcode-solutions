from itertools import product
import re
import unittest

from python.p0068_text_justification import Solution


class JustificationIndependentContractTests(unittest.TestCase):
    def check(self, words, width):
        before = words[:]
        result = Solution().fullJustify(words, width)
        self.assertIs(type(result), list)
        self.assertTrue(result)
        offset = 0
        for index, line in enumerate(result):
            self.assertIs(type(line), str)
            self.assertEqual(len(line), width)
            self.assertFalse(line.startswith(' '))
            tokens = [token for token in line.split(' ') if token]
            self.assertTrue(tokens)
            self.assertEqual(tokens, words[offset:offset + len(tokens)])
            offset += len(tokens)
            minimum = sum(map(len, tokens)) + len(tokens) - 1
            if offset < len(words):
                self.assertGreater(minimum + 1 + len(words[offset]), width)
            if index == len(result) - 1 or len(tokens) == 1:
                self.assertEqual(line, ' '.join(tokens).ljust(width))
            else:
                self.assertFalse(line.endswith(' '))
                gaps = list(map(len, re.findall(' +', line)))
                self.assertEqual(len(gaps), len(tokens) - 1)
                self.assertGreaterEqual(min(gaps), 1)
                self.assertLessEqual(max(gaps) - min(gaps), 1)
                self.assertEqual(gaps, sorted(gaps, reverse=True))
        self.assertEqual(offset, len(words))
        self.assertEqual(words, before)
        return result

    def test_all_small_word_sequences_against_layout_invariants(self):
        inputs = checks = 0
        for size in range(1, 7):
            for words in product(('a', 'bb', 'C!'), repeat=size):
                inputs += 1
                for width in range(3, 9):
                    self.check(list(words), width)
                    checks += 1
        self.assertEqual((inputs, checks), (1092, 6552))

    def test_maximum_count_width_word_length_and_last_line(self):
        self.assertEqual(len(self.check(['x'] * 300, 100)), 6)
        self.assertEqual(len(self.check(['z' * 20] * 300, 20)), 300)
        self.check(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16)
        self.check(['What', 'must', 'be', 'acknowledgment', 'shall', 'be'], 16)
        self.check(['a'], 1)
        self.check(['a', 'b', 'c', 'd'], 3)


if __name__ == '__main__':
    unittest.main()
