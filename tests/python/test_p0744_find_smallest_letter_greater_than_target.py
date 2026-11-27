import string
import unittest
from itertools import combinations_with_replacement

from python.p0744_find_smallest_letter_greater_than_target import Solution


class NextGreaterLetterTests(unittest.TestCase):
    def check(self, letters, target, expected=None):
        before = letters[:]
        expected = next((letter for letter in letters if letter > target), letters[0]) if expected is None else expected
        result = Solution().nextGreatestLetter(letters, target)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(letters, before)

    def test_all_small_legal_sorted_multisets_and_all_alphabet_targets_against_scan(self):
        arrays = queries = 0
        for size in range(2, 9):
            for values in combinations_with_replacement('acz', size):
                if len(set(values)) < 2:
                    continue
                arrays += 1
                for target in string.ascii_lowercase:
                    self.check(list(values), target)
                    queries += 1
        self.assertEqual((arrays, queries), (140, 3640))

    def test_examples_duplicate_blocks_and_ten_thousand_letters(self):
        self.check(['c','f','j'], 'a', 'c')
        self.check(['c','f','j'], 'c', 'f')
        self.check(['x','x','y','y'], 'z', 'x')
        for target, expected in (('a','z'),('b','z'),('y','z'),('z','a')):
            self.check(['a'] * 5000 + ['z'] * 5000, target, expected)
        self.check(['c'] * 5000 + ['f'] * 5000, 'd', 'f')
        self.check(['c'] * 5000 + ['f'] * 5000, 'z', 'c')


if __name__ == '__main__':
    unittest.main()
