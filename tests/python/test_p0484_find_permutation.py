from itertools import permutations, product
import unittest

from python.p0484_find_permutation import Solution


def first_valid_permutation(pattern):
    for values in permutations(range(1, len(pattern) + 2)):
        if all((values[index] < values[index + 1]) == (char == 'I')
               for index, char in enumerate(pattern)):
            return list(values)
    raise AssertionError('a permutation must exist for every I/D pattern')


class DescendingRunPermutationTests(unittest.TestCase):
    def check(self, pattern, expected=None):
        actual = Solution().findPermutation(pattern)
        self.assertEqual(actual, first_valid_permutation(pattern) if expected is None else expected)
        self.assertEqual(sorted(actual), list(range(1, len(pattern) + 2)))
        self.assertTrue(all((actual[index] < actual[index + 1]) == (char == 'I')
                            for index, char in enumerate(pattern)))

    def test_all_short_patterns_against_lexicographic_permutation_enumeration(self):
        patterns = 0
        for size in range(7):
            for chars in product('ID', repeat=size):
                self.check(''.join(chars))
                patterns += 1
        self.assertEqual(patterns, 127)

    def test_maximum_patterns_whole_run_and_alternating_boundaries(self):
        self.check('I' * 100000, list(range(1, 100002)))
        self.check('D' * 100000, list(range(100001, 0, -1)))
        alternating = [1] + [value for pair in range(2, 100001, 2) for value in (pair + 1, pair)]
        self.check('ID' * 50000, alternating)
        self.check('DI', [2, 1, 3])
        self.check('DDIIDI', [3, 2, 1, 4, 6, 5, 7])


if __name__ == '__main__':
    unittest.main()
