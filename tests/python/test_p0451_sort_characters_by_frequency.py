from collections import Counter
from itertools import groupby, product
import string
import unittest

from python.p0451_sort_characters_by_frequency import Solution


class FrequencyBlockOrderingTests(unittest.TestCase):
    def check(self, text):
        result = Solution().frequencySort(text)
        self.assertIs(type(result), str)
        self.assertEqual(Counter(result), Counter(text))
        blocks = [(letter, len(list(group))) for letter, group in groupby(result)]
        self.assertEqual(len(blocks), len(set(text)))
        frequencies = [length for _, length in blocks]
        self.assertEqual(frequencies, sorted(frequencies, reverse=True))

    def test_all_small_case_and_digit_strings_against_output_constraints(self):
        checks = 0
        for size in range(1, 9):
            for letters in product('aA0', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_all_62_characters_and_tied_blocks(self):
        self.check('a' * 250000 + 'A' * 125000 + '0' * 125000)
        alphabet = string.ascii_letters + string.digits
        text = alphabet * 8064 + alphabet[:32]
        self.assertEqual(len(text), 500000)
        self.check(text)
        self.check('cccaaa')
        self.check('Aabb')


if __name__ == '__main__':
    unittest.main()
