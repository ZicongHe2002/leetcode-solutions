from itertools import product
import unittest

from python.p0423_reconstruct_original_digits_from_english import Solution


WORDS = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')


class DigitWordMultisetTests(unittest.TestCase):
    def check(self, text, expected):
        result = Solution().originalDigits(text)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(result, ''.join(sorted(result)))

    def test_every_small_digit_multiset_with_scrambled_letter_order(self):
        multisets = 0
        for counts in product(range(3), repeat=10):
            text = ''.join(word * count for word, count in zip(WORDS, counts))
            scrambled = ''.join(sorted(text))
            split = len(scrambled) // 3
            scrambled = (scrambled[split:] + scrambled[:split])[::-1]
            expected = ''.join(str(digit) * count for digit, count in enumerate(counts))
            self.check(scrambled, expected)
            multisets += 1
        self.assertEqual(multisets, 59049)

    def test_unique_letters_cancellation_and_maximum_input_length(self):
        self.check('owoztneoer', '012')
        self.check('fviefuro', '45')
        self.check('zero' * 25000, '0' * 25000)
        self.check('eight' * 20000, '8' * 20000)
        text = ''.join(WORDS) * 2500
        self.assertEqual(len(text), 100000)
        self.check(text[::-1], ''.join(str(digit) * 2500 for digit in range(10)))
        self.check('', '')


if __name__ == '__main__':
    unittest.main()
