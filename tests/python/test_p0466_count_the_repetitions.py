from itertools import product
import unittest

from python.p0466_count_the_repetitions import Solution


def lcs_contains(source, target):
    row = [0] * (len(target) + 1)
    for char in source:
        diagonal = 0
        for index, expected in enumerate(target, 1):
            old = row[index]
            row[index] = diagonal + 1 if char == expected else max(row[index], row[index - 1])
            diagonal = old
    return row[-1] == len(target)


def short_lcs_repetition_oracle(s1, n1, s2, n2):
    source, target = s1 * n1, s2 * n2
    return max(count for count in range(len(source) // len(target) + 1)
               if lcs_contains(source, target * count))


class RepetitionBoundaryStateTests(unittest.TestCase):
    def check(self, s1, n1, s2, n2, expected=None):
        actual = Solution().getMaxRepetitions(s1, n1, s2, n2)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, short_lcs_repetition_oracle(s1, n1, s2, n2) if expected is None else expected)

    def test_all_short_patterns_repeats_and_group_sizes_against_lcs(self):
        patterns = [''.join(chars) for size in range(1, 4) for chars in product('ab', repeat=size)]
        queries = 0
        for s1 in patterns:
            for s2 in patterns:
                for n1 in range(7):
                    for n2 in range(1, 5):
                        self.check(s1, n1, s2, n2)
                        queries += 1
        self.assertEqual(queries, 5488)

    def test_million_repeats_long_patterns_and_cross_block_remainders(self):
        self.check('a' * 100, 10**6, 'a', 1, 10**8)
        self.check('a' * 100, 10**6, 'a' * 100, 10**6, 1)
        self.check('ab', 10**6, 'ba', 1, 999999)
        self.check('ab', 10**6, 'ba', 999999, 1)
        self.check('ab', 2, 'bab', 1, 1)
        self.check('abc', 10**6, 'acb', 1, 500000)
        self.check('ab', 10**6, 'c', 1, 0)
        self.check('acb', 4, 'ab', 2, 2)


if __name__ == '__main__':
    unittest.main()
