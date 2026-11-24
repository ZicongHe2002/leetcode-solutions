import unittest
from itertools import product

from python.p0017_phone_letter_combinations import Solution


KEYS = dict(zip('23456789', ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')))


class PhoneLetterTests(unittest.TestCase):
    def check(self, digits):
        expected = [''.join(items) for items in product(*(KEYS[digit] for digit in digits))] if digits else []
        actual = Solution().letterCombinations(digits)
        self.assertEqual(sorted(actual), sorted(expected))
        for item in actual:
            self.assertEqual(len(item), len(digits))
            self.assertTrue(all(letter in KEYS[digit] for letter, digit in zip(item, digits)))
        return actual

    def test_all_legal_digit_strings_against_cartesian_product(self):
        checks = 0
        for size in range(5):
            for digits in product('23456789', repeat=size):
                self.check(''.join(digits))
                checks += 1
        self.assertEqual(checks, 4681)

    def test_explicit_mapping_four_letter_keys_and_empty_input(self):
        self.assertEqual(sorted(self.check('23')), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
        self.assertEqual(len(self.check('79')), 16)
        self.assertEqual(len(self.check('7777')), 256)
        self.assertEqual(len(self.check('9999')), 256)
        self.assertEqual(self.check(''), [])


if __name__ == '__main__':
    unittest.main()
