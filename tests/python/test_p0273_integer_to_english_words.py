from itertools import product
import unittest

from python.p0273_integer_to_english_words import Solution


SMALL_VALUES = dict(zip('One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split(), range(1, 20)))
TENS_VALUES = dict(zip('Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(), range(20, 100, 10)))
SCALES = {'Billion': 10**9, 'Million': 10**6, 'Thousand': 1000}


def parse_group(tokens):
    if not tokens:
        raise AssertionError('empty magnitude group')
    value = 0
    if len(tokens) >= 2 and tokens[1] == 'Hundred':
        assert tokens[0] in SMALL_VALUES and SMALL_VALUES[tokens[0]] < 10
        value = SMALL_VALUES[tokens[0]] * 100
        tokens = tokens[2:]
    if not tokens:
        return value
    if tokens[0] in SMALL_VALUES:
        assert len(tokens) == 1
        return value + SMALL_VALUES[tokens[0]]
    assert tokens[0] in TENS_VALUES and len(tokens) in (1, 2)
    value += TENS_VALUES[tokens[0]]
    if len(tokens) == 2:
        assert tokens[1] in SMALL_VALUES and SMALL_VALUES[tokens[1]] < 10
        value += SMALL_VALUES[tokens[1]]
    return value


def grammar_roundtrip(text):
    assert text and text == ' '.join(text.split())
    if text == 'Zero':
        return 0
    total = 0
    current = []
    previous_scale = 10**12
    for token in text.split(' '):
        if token in SCALES:
            scale = SCALES[token]
            assert scale < previous_scale
            total += parse_group(current) * scale
            current = []
            previous_scale = scale
        else:
            current.append(token)
    if current:
        total += parse_group(current)
    return total


class EnglishNumberGrammarTests(unittest.TestCase):
    def check(self, value, expected=None):
        text = Solution().numberToWords(value)
        self.assertIs(type(text), str)
        self.assertEqual(grammar_roundtrip(text), value)
        if expected is not None:
            self.assertEqual(text, expected)

    def test_small_values_and_all_legal_three_digit_magnitude_groups(self):
        for value in range(10000):
            self.check(value)
        for group in range(1000):
            for scale in (1, 1000, 10**6, 10**9):
                value = group * scale
                if value <= 2**31 - 1:
                    self.check(value)

    def test_sparse_groups_mixed_groups_and_maximum_int32_text(self):
        choices = (0, 1, 10, 11, 19, 20, 21, 99, 100, 101, 110, 999)
        for million, thousand, units in product(choices, repeat=3):
            self.check(million * 10**6 + thousand * 1000 + units)
        self.check(0, 'Zero')
        self.check(1000001, 'One Million One')
        self.check(1000010, 'One Million Ten')
        self.check(2**31 - 1, 'Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven')


if __name__ == '__main__':
    unittest.main()
