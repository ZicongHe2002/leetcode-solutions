import unittest
from itertools import product

from python.p0748_shortest_completing_word import Solution


def consume_literal_letters(plate, words):
    required = [char.lower() for char in plate if 'a' <= char.lower() <= 'z']
    valid = []
    for index, word in enumerate(words):
        remaining = list(word)
        for char in required:
            if char not in remaining:
                break
            remaining.remove(char)
        else:
            valid.append((len(word), index, word))
    return min(valid)[2] if valid else None


class ShortestCompletingWordTests(unittest.TestCase):
    def check(self, plate, words, expected=None):
        before = words[:]
        result = Solution().shortestCompletingWord(plate, words)
        self.assertIs(type(result), str)
        self.assertEqual(result, consume_literal_letters(plate, words) if expected is None else expected, (plate, words[:10]))
        self.assertEqual(words, before)

    def test_all_short_mixed_plates_and_word_lists_with_guaranteed_answers_against_character_consumption(self):
        plates = [''.join(chars) for size in range(1, 4) for chars in product('aAbB0 ', repeat=size)]
        pool = [''.join(chars) for size in range(1, 4) for chars in product('ab', repeat=size)]
        lists = [list(words) for size in (1, 2) for words in product(pool, repeat=size)]
        self.assertEqual((len(plates), len(lists)), (258, 210))
        examined = checked = 0
        for plate, words in product(plates, lists):
            expected = consume_literal_letters(plate, words)
            examined += 1
            if expected is not None:
                self.check(plate, words, expected)
                checked += 1
        self.assertEqual(examined, 54180)
        self.assertGreater(checked, 10000)

    def test_examples_multiplicity_stable_ties_empty_requirements_and_maximum_sizes(self):
        self.check('1s3 PSt', ['step','steps','stripe','stepple'], 'steps')
        self.check('1s3 456', ['looks','pest','stew','show'], 'pest')
        self.check('AA b', ['ab','bbaa','aba'], 'aba')
        self.check('123 456', ['aaaa','b','c'], 'b')
        self.check(' ', ['bbb','aa','ab'], 'aa')
        words = ['z' * 15] * 998 + ['cabaz','abcaa']
        self.assertEqual(len(words), 1000)
        self.check('A1b C2a', words, 'cabaz')
        self.check('AAAAAAA', ['a' * 14 + 'z'] * 999 + ['a' * 7], 'a' * 7)


if __name__ == '__main__':
    unittest.main()
