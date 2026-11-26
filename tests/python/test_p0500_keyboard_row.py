from itertools import product
import re
import unittest

from python.p0500_keyboard_row import Solution


ROW_PATTERNS = [re.compile(pattern, re.IGNORECASE | re.ASCII)
                for pattern in (r'[qwertyuiop]+', r'[asdfghjkl]+', r'[zxcvbnm]+')]


def full_row_grammar_oracle(words):
    return [word for word in words if any(pattern.fullmatch(word) for pattern in ROW_PATTERNS)]


class KeyboardRowSubsetTests(unittest.TestCase):
    def check(self, words, expected=None):
        before = words[:]
        actual = Solution().findWords(words)
        self.assertIs(type(actual), list)
        self.assertEqual(actual, full_row_grammar_oracle(words) if expected is None else expected)
        self.assertEqual(words, before)

    def test_every_short_case_variant_word_in_bounded_batches_against_full_grammar(self):
        words = [''.join(chars) for size in range(1, 6) for chars in product('qQaAzZ', repeat=size)]
        batches = 0
        for start in range(0, len(words), 20):
            self.check(words[start:start + 20])
            batches += 1
        self.assertEqual((len(words), batches), (9330, 467))

    def test_maximum_word_count_length_original_case_duplicates_and_empty_extension(self):
        words = ['QwErTyUiOp' * 10, 'AsDfGhJkL' * 11 + 'A', 'zXcVbNm' * 14 + 'zX', 'q' * 99 + 'A'] * 5
        self.assertEqual((len(words), set(map(len, words))), (20, {100}))
        self.check(words)
        self.check(['Hello', 'Alaska', 'Dad', 'Peace'], ['Alaska', 'Dad'])
        self.check(['qQ', 'qQ', 'A', 'Z'], ['qQ', 'qQ', 'A', 'Z'])
        self.check([], [])


if __name__ == '__main__':
    unittest.main()
