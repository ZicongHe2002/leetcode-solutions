import random
import string
import unittest
from itertools import combinations_with_replacement, product

from python.p0804_unique_morse_code_words import Solution


def binary_tree_codes():
    codes = {}
    for depth,letters in enumerate(('','et','ianm','surwdkgo','hvf l pjbxcyzq  ')):
        if depth == 0:
            continue
        assert len(letters) == 2**depth
        for position,letter in enumerate(letters):
            if letter != ' ':
                codes[letter] = tuple(bool(position >> bit & 1) for bit in range(depth - 1,-1,-1))
    return codes


def tree_encoding(word, codes):
    return tuple(edge for letter in word for edge in codes[letter])


class UniqueMorseTests(unittest.TestCase):
    def check(self, words, expected):
        before = words[:]
        result = Solution().uniqueMorseRepresentations(words)
        self.assertIs(type(result),int)
        self.assertEqual(result,expected,words)
        self.assertEqual(words,before)

    def test_all_one_two_letter_word_pairs_against_independent_morse_tree_paths(self):
        codes = binary_tree_codes()
        self.assertEqual(set(codes),set(string.ascii_lowercase))
        words = [''.join(chars) for size in (1,2) for chars in product(string.ascii_lowercase,repeat=size)]
        encodings = {word:tree_encoding(word,codes) for word in words}
        checked = 0
        for first,second in combinations_with_replacement(words,2):
            self.check([first,second],1 if encodings[first] == encodings[second] else 2)
            checked += 1
        self.assertEqual((len(words),checked),(702,246753))

    def test_examples_boundaries_and_seeded_word_batches(self):
        self.check(['gin','zen','gig','msg'],2)
        self.check(['a'],1)
        self.check(['a','et'],1)
        self.check(list(string.ascii_lowercase),26)
        self.check(['z' * 12] * 100,1)
        generator,codes = random.Random(804),binary_tree_codes()
        for _ in range(100):
            words = [''.join(generator.choice(string.ascii_lowercase) for _ in range(generator.randrange(1,13)))
                     for _ in range(generator.randrange(1,101))]
            self.check(words,len({tree_encoding(word,codes) for word in words}))


if __name__ == '__main__':
    unittest.main()
