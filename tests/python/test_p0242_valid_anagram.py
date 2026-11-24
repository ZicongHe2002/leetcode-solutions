import unittest
from itertools import product

from python.p0242_valid_anagram import Solution


class AnagramTests(unittest.TestCase):
    def test_all_small_string_pairs_against_sorting(self):
        strings = [''.join(chars) for size in range(5) for chars in product('abc', repeat=size)]
        self.assertEqual(len(strings), 121)
        for first in strings:
            for second in strings:
                self.assertEqual(Solution().isAnagram(first, second), sorted(first) == sorted(second))

    def test_count_mismatch_and_maximum_length(self):
        for first, second, expected in [('aab', 'abb', False), ('aabb', 'bbaa', True),
                                         ('a', 'aa', False), ('z', 'z', True),
                                         ('a' * 50000, 'a' * 49999 + 'z', False),
                                         ('a' * 25000 + 'z' * 25000, 'za' * 25000, True)]:
            self.assertEqual(Solution().isAnagram(first, second), expected)


if __name__ == '__main__':
    unittest.main()
