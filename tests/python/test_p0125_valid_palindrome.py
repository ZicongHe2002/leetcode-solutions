import unittest
from itertools import product

from python.p0125_valid_palindrome import Solution


def oracle(text):
    filtered = ''.join(character.lower() for character in text
                       if character.isascii() and character.isalnum())
    return filtered == filtered[::-1]


class PalindromeTests(unittest.TestCase):
    def test_small_strings_and_all_printable_ascii_pairs(self):
        checked = 0
        for size in range(6):
            for letters in product('aAbB01 ,', repeat=size):
                text = ''.join(letters)
                self.assertEqual(Solution().isPalindrome(text), oracle(text))
                checked += 1
        self.assertEqual(checked, 37449)
        printable = ''.join(chr(value) for value in range(32, 127))
        self.assertEqual(len(printable), 95)
        for first in printable:
            for second in printable:
                text = first + second
                self.assertEqual(Solution().isPalindrome(text), oracle(text))

    def test_examples_and_maximum_length(self):
        for text, expected in [('A man, a plan, a canal: Panama', True), ('race a car', False),
                                ('0P', False), ('0,P!0', True), (' ', True), ('ab_a', True)]:
            self.assertIs(Solution().isPalindrome(text), expected)
        self.assertTrue(Solution().isPalindrome(',' * 200000))
        self.assertTrue(Solution().isPalindrome('A' * 200000))
        self.assertFalse(Solution().isPalindrome('A' * 199999 + 'b'))


if __name__ == '__main__':
    unittest.main()
