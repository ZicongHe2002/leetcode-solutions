import unittest
from itertools import product

from python.p0647_palindromic_substrings import Solution


def all_intervals_oracle(text):
    return sum(text[left:right] == text[left:right][::-1] for left in range(len(text))
               for right in range(left + 1, len(text) + 1))


class PalindromeCountTests(unittest.TestCase):
    def test_all_small_ternary_strings_against_all_intervals(self):
        checks = 0
        for size in range(9):
            for letters in product('abc', repeat=size):
                text = ''.join(letters)
                self.assertEqual(Solution().countSubstrings(text), all_intervals_oracle(text))
                checks += 1
        self.assertEqual(checks, 9841)

    def test_occurrence_count_and_maximum_length(self):
        for text, expected in [('aaa', 6), ('abc', 3), ('a' * 1000, 500500),
                               ('a' * 500 + 'b' * 500, 250500),
                               ('abc' * 333 + 'a', 1000), ('', 0)]:
            self.assertEqual(Solution().countSubstrings(text), expected)


if __name__ == '__main__':
    unittest.main()
