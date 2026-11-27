from collections import Counter
from itertools import product
import unittest

from python.p0187_repeated_dna_sequences import Solution


def substring_counter_oracle(text):
    counts = Counter(text[index:index + 10] for index in range(len(text) - 9))
    return {window for window, count in counts.items() if count >= 2}


class DnaExactEncodingTests(unittest.TestCase):
    def check(self, text, expected=None):
        result = Solution().findRepeatedDnaSequences(text)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(window) is str and len(window) == 10 for window in result))
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(set(result), substring_counter_oracle(text) if expected is None else expected)

    def test_all_small_binary_dna_against_explicit_window_counts(self):
        strings = 0
        for size in range(13):
            for characters in product('AC', repeat=size):
                self.check(''.join(characters))
                strings += 1
        self.assertEqual(strings, 8191)

    def test_full_alphabet_overlap_window_length_and_maximum_input(self):
        self.check('ACGTACGTAC', set())
        self.check('A' * 11, {'A' * 10})
        self.check('A' * 12, {'A' * 10})
        self.check(''.join(''.join(word) for word in product('ACGT', repeat=5)))
        self.check('A' * 100000, {'A' * 10})
        cycle = 'ACGT' * 25000
        self.check(cycle, {cycle[index:index + 10] for index in range(4)})


if __name__ == '__main__':
    unittest.main()
