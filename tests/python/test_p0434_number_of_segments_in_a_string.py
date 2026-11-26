from itertools import product
import unittest

from python.p0434_number_of_segments_in_a_string import Solution


class SegmentStartTests(unittest.TestCase):
    def test_all_small_strings_against_explicit_split_and_filter(self):
        strings = 0
        for size in range(8):
            for characters in product('a !', repeat=size):
                text = ''.join(characters)
                expected = len([piece for piece in text.split(' ') if piece])
                actual = Solution().countSegments(text)
                self.assertIs(type(actual), int)
                self.assertEqual(actual, expected)
                strings += 1
        self.assertEqual(strings, 3280)

    def test_punctuation_digits_spacing_and_maximum_length(self):
        for text, expected in [('', 0), ('   ', 0), ('  a  b   c ', 3), ('a,b', 1), ('!@#$%', 1), ('12 34', 2), ('Hello, my name is John', 5)]:
            self.assertEqual(Solution().countSegments(text), expected)
        self.assertEqual(Solution().countSegments(' ' * 300), 0)
        self.assertEqual(Solution().countSegments('a ' * 150), 150)
        self.assertEqual(Solution().countSegments('a' * 300), 1)


if __name__ == '__main__':
    unittest.main()
