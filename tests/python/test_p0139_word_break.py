import unittest
from itertools import islice, product

from python.p0139_word_break import Solution


def cut_mask_oracle(s, dictionary):
    if not s:
        return True
    words = set(dictionary)
    for mask in range(1 << (len(s) - 1)):
        cuts = [0] + [index + 1 for index in range(len(s) - 1) if mask & (1 << index)] + [len(s)]
        if all(s[left:right] in words for left, right in zip(cuts, cuts[1:])):
            return True
    return False


class WordBreakTests(unittest.TestCase):
    def check(self, text, dictionary, expected):
        before = dictionary[:]
        self.assertIs(Solution().wordBreak(text, dictionary), expected)
        self.assertEqual(dictionary, before)

    def test_all_small_dictionary_subsets_and_binary_strings_against_cut_masks(self):
        vocabulary = ['a', 'b', 'aa', 'ab', 'ba', 'bb']
        texts = [''.join(chars) for size in range(7) for chars in product('ab', repeat=size)]
        checks = 0
        for mask in range(1 << len(vocabulary)):
            dictionary = [word for index, word in enumerate(vocabulary) if mask & (1 << index)]
            for text in texts:
                self.check(text, dictionary, cut_mask_oracle(text, dictionary))
                checks += 1
        self.assertEqual(checks, 8128)

    def test_examples_maximum_sizes_and_empty_extensions(self):
        self.check('leetcode', ['leet', 'code'], True)
        self.check('applepenapple', ['apple', 'pen'], True)
        self.check('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'], False)
        self.check('a' * 300, ['a' * 20], True)
        self.check('a' * 299 + 'b', ['a' * size for size in range(1, 21)], False)
        dictionary = [''.join(chars) for chars in islice(product('abcde', repeat=5), 1000)]
        self.assertEqual(len(set(dictionary)), 1000)
        self.check('z' * 300, dictionary, False)
        self.check('', [], True)
        self.check('a', [], False)


if __name__ == '__main__':
    unittest.main()
