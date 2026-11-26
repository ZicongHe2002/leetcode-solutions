from itertools import product
import unittest

from python.p0344_reverse_string import Solution


class InPlaceCharacterReverseTests(unittest.TestCase):
    def check(self, text):
        values = list(text)
        alias = values
        result = Solution().reverseString(values)
        self.assertIsNone(result)
        self.assertIs(values, alias)
        self.assertEqual(values, list(text[::-1]))

    def test_all_small_character_arrays(self):
        inputs = 0
        for size in range(9):
            for chars in product('abc', repeat=size):
                self.check(''.join(chars))
                inputs += 1
        self.assertEqual(inputs, 9841)

    def test_ascii_domain_and_maximum_length(self):
        self.check(''.join(chr(value) for value in range(32, 127)))
        self.check('ab' * 50000)
        self.check('z' * 100000)
        self.check('a')
        self.check('abcd')
        self.check('abcde')


if __name__ == '__main__':
    unittest.main()
