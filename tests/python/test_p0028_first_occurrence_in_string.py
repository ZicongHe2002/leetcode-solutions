import unittest
from itertools import product

from python.p0028_first_occurrence_in_string import Solution


class FirstOccurrenceTests(unittest.TestCase):
    def check(self, haystack, needle):
        result = Solution().strStr(haystack, needle)
        self.assertIs(type(result), int)
        self.assertEqual(result, haystack.find(needle))

    def test_all_small_binary_strings_and_empty_extensions_against_find(self):
        haystacks = [''.join(chars) for size in range(6) for chars in product('ab', repeat=size)]
        needles = [''.join(chars) for size in range(5) for chars in product('ab', repeat=size)]
        checks = 0
        for haystack in haystacks:
            for needle in needles:
                self.check(haystack, needle)
                checks += 1
        self.assertEqual(checks, 1953)

    def test_maximum_lengths_repeated_borders_and_first_match(self):
        self.check('a' * 9999 + 'b', 'a' * 4999 + 'b')
        self.check('a' * 10000, 'a' * 10000)
        self.check('a', 'a' * 10000)
        self.check('ababababacabad', 'ababaca')
        self.check('mississippi', 'issi')


if __name__ == '__main__':
    unittest.main()
