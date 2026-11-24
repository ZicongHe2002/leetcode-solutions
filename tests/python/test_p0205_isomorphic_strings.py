import unittest
from itertools import product

from python.p0205_isomorphic_strings import Solution


class IsomorphicTests(unittest.TestCase):
    def check(self, left, right, expected=None):
        if expected is None:
            expected = len(left) == len(right) and all((left[i] == left[j]) == (right[i] == right[j])
                                                      for i in range(len(left)) for j in range(len(left)))
        result = Solution().isIsomorphic(left, right)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_all_small_equal_length_words_against_position_equivalence(self):
        checks = 0
        for size in range(1, 5):
            words = [''.join(chars) for chars in product('abc', repeat=size)]
            for left in words:
                for right in words:
                    self.check(left, right)
                    checks += 1
        self.assertEqual(checks, 7380)

    def test_maximum_length_collisions_ascii_and_empty_extensions(self):
        self.check('ab' * 25000, 'xy' * 25000, True)
        self.check('ab' * 25000, 'x' * 50000, False)
        self.check(' @', 'a#', True)
        self.check('ab', 'aa', False)
        self.check('', '', True)
        self.check('ab', 'a', False)


if __name__ == '__main__':
    unittest.main()
