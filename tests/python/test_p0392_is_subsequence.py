import unittest
from itertools import product

from python.p0392_is_subsequence import Solution


def all_subsequences(word):
    return {''.join(character for index, character in enumerate(word) if mask & (1 << index))
            for mask in range(1 << len(word))}


class SubsequenceTests(unittest.TestCase):
    def check(self, source, target, expected):
        result = Solution().isSubsequence(source, target)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_all_small_binary_pairs_against_explicit_subsequences(self):
        sources = [''.join(chars) for size in range(5) for chars in product('ab', repeat=size)]
        targets = [''.join(chars) for size in range(8) for chars in product('ab', repeat=size)]
        checks = 0
        for target in targets:
            possible = all_subsequences(target)
            for source in sources:
                self.check(source, target, source in possible)
                checks += 1
        self.assertEqual(checks, 7905)

    def test_maximum_lengths_order_repetition_and_empty_inputs(self):
        self.check('a' * 100, 'a' * 10000, True)
        self.check('a' * 99 + 'b', 'a' * 10000, False)
        self.check('ba', 'a' * 9999 + 'b', False)
        self.check('', 'a' * 10000, True)
        self.check('a', '', False)
        self.check('', '', True)


if __name__ == '__main__':
    unittest.main()
