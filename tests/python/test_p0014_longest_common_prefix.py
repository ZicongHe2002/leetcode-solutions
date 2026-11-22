import unittest
from itertools import product

from python.p0014_longest_common_prefix import Solution


class CommonPrefixTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        if values:
            prefixes = [{word[:size] for size in range(len(word) + 1)} for word in values]
            expected = max(set.intersection(*prefixes), key=len)
        else:
            expected = ''
        result = Solution().longestCommonPrefix(values)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_word_lists_against_prefix_set_intersection(self):
        words = [''.join(chars) for size in range(4) for chars in product('ab', repeat=size)]
        checks = 0
        for size in range(1, 4):
            for values in product(words, repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 3615)

    def test_maximum_count_length_short_word_and_empty_list_extension(self):
        self.check(['a' * 200] * 199 + ['a' * 199 + 'b'])
        self.check(['a' * 200] * 200)
        self.check(['a' * 200, ''])
        self.check(['abc'])
        self.check([])


if __name__ == '__main__':
    unittest.main()
