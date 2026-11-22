import unittest
from itertools import product

from python.p0132_palindrome_partitioning_ii import Solution


def minimum_cuts_by_all_boundaries(text):
    if not text:
        return 0
    best = len(text) - 1
    for mask in range(1 << (len(text) - 1)):
        count = mask.bit_count()
        if count >= best:
            continue
        start = 0
        valid = True
        for end in range(1, len(text) + 1):
            if end == len(text) or mask >> (end - 1) & 1:
                piece = text[start:end]
                if piece != piece[::-1]:
                    valid = False
                    break
                start = end
        if valid:
            best = count
    return best


class PalindromeCutTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = minimum_cuts_by_all_boundaries(text)
        result = Solution().minCut(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, text)

    def test_all_small_ternary_strings_against_cut_subsets(self):
        checks = 0
        for size in range(1, 8):
            for values in product('abc', repeat=size):
                self.check(''.join(values))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_lengths_odd_even_centers_alternation_and_empty_extension(self):
        self.check('a' * 2000, 0)
        self.check('ab' * 1000, 1)
        self.check('abc' * 666 + 'ab', 1999)
        self.check('a' * 999 + 'bb' + 'a' * 999, 0)
        self.check('a' * 1999 + 'b', 1)
        self.check('', 0)


if __name__ == '__main__':
    unittest.main()
