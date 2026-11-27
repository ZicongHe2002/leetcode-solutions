import random
import unittest
from itertools import product

from python.p0648_replace_words import Solution


def all_roots(dictionary, sentence):
    return ' '.join(min((root for root in dictionary if word.startswith(root)),
                        key=len, default=word) for word in sentence.split(' '))


class ReplaceWordTests(unittest.TestCase):
    def check(self, dictionary, sentence, expected=None):
        before = dictionary[:]
        if expected is None:
            expected = all_roots(dictionary, sentence)
        result = Solution().replaceWords(dictionary, sentence)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(dictionary, before)

    def test_all_short_root_subsets_and_seeded_samples_against_full_root_scan(self):
        kinds = ['a', 'b', 'aa', 'ab', 'ba', 'bb']
        words = [''.join(chars) for length in range(1, 6) for chars in product('ab', repeat=length)]
        self.assertEqual(len(words), 62)
        for mask in range(1, 1 << len(kinds)):
            self.check([root for index, root in enumerate(kinds) if mask & (1 << index)], ' '.join(words))
        rng = random.Random(648)
        for _ in range(500):
            dictionary = [''.join(rng.choice('abc') for _ in range(rng.randint(1, 8)))
                          for _ in range(rng.randint(1, 15))]
            sentence = ' '.join(''.join(rng.choice('abc') for _ in range(rng.randint(1, 20)))
                                for _ in range(rng.randint(1, 20)))
            self.check(dictionary, sentence)

    def test_maximum_dictionary_sentence_and_shortest_terminal(self):
        dictionary = ['a' * 97 + chr(97 + index // 676)
                      + chr(97 + index // 26 % 26) + chr(97 + index % 26)
                      for index in range(999)] + ['z']
        sentence = ' '.join(['z' * 1000] + ['z' * 999] * 999)
        self.assertEqual((len(dictionary), len(sentence)), (1000, 1000000))
        self.check(dictionary, sentence, ' '.join(['z'] * 1000))
        self.check(['abc', 'ab', 'a'], 'abcd abc ab a x', 'a a a a x')
        self.check(['ab', 'ab'], 'ab abc a', 'ab ab a')
        self.check(['cat', 'bat', 'rat'], 'the cattle was rattled by the battery', 'the cat was rat by the bat')


if __name__ == '__main__':
    unittest.main()
