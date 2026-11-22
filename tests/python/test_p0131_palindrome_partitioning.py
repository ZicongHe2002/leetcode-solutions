import unittest
from itertools import product

from python.p0131_palindrome_partitioning import Solution


def cut_mask_oracle(s):
    if not s:
        return [()]
    answers = []
    for mask in range(1 << (len(s) - 1)):
        cuts = [0] + [index + 1 for index in range(len(s) - 1) if mask & (1 << index)] + [len(s)]
        pieces = tuple(s[left:right] for left, right in zip(cuts, cuts[1:]))
        if all(piece == piece[::-1] for piece in pieces):
            answers.append(pieces)
    return answers


class PalindromePartitionTests(unittest.TestCase):
    def check(self, s):
        actual = Solution().partition(s)
        self.assertEqual(sorted(map(tuple, actual)), sorted(cut_mask_oracle(s)))
        self.assertEqual(len({id(row) for row in actual}), len(actual))
        for pieces in actual:
            self.assertEqual(''.join(pieces), s)
            self.assertTrue(all(piece and piece == piece[::-1] for piece in pieces))
        return actual

    def test_all_small_binary_strings_against_cut_masks(self):
        checks = 0
        for size in range(1, 9):
            for letters in product('ab', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 510)

    def test_examples_maximum_length_and_empty_extension(self):
        self.assertEqual(sorted(map(tuple, self.check('aab'))), [('a', 'a', 'b'), ('aa', 'b')])
        self.assertEqual(len(self.check('a' * 16)), 32768)
        self.assertEqual(self.check('abcdefghijklmnop'), [list('abcdefghijklmnop')])
        self.assertEqual(self.check(''), [[]])


if __name__ == '__main__':
    unittest.main()
