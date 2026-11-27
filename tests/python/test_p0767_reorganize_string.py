import unittest
from collections import Counter
from itertools import product

from python.p0767_reorganize_string import Solution


class ReorganizeStringTests(unittest.TestCase):
    def check(self, text, possible):
        result = Solution().reorganizeString(text)
        self.assertIs(type(result), str)
        if possible:
            self.assertEqual(Counter(result), Counter(text), text)
            self.assertEqual(len(result), len(text))
            self.assertTrue(all(a != b for a, b in zip(result, result[1:])), (text, result))
        else:
            self.assertEqual(result, '', text)

    def test_all_small_strings_against_complete_valid_output_universe(self):
        checked = 0
        for size in range(1, 9):
            texts = [''.join(chars) for chars in product('abc', repeat=size)]
            feasible = {''.join(sorted(text)) for text in texts if all(a != b for a,b in zip(text,text[1:]))}
            for text in texts:
                self.check(text, ''.join(sorted(text)) in feasible)
                checked += 1
        self.assertEqual(checked, 9840)

    def test_official_examples_maximum_lengths_and_odd_even_frequency_limits(self):
        self.check('aab', True)
        self.check('aaab', False)
        self.check('a', True)
        self.check('a' * 250 + 'b' * 250, True)
        self.check('a' * 251 + 'b' * 249, False)
        self.check('a' * 250 + 'b' * 249, True)
        self.check('a' * 250 + 'b' * 249 + 'c', True)
        self.check(''.join(chr(97 + index % 26) for index in range(500)), True)


if __name__ == '__main__':
    unittest.main()
