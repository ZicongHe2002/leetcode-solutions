import unittest
from collections import Counter
from itertools import product

from python.p0115_distinct_subsequences import Solution


def counted_position_choices(word):
    return Counter(''.join(character for index, character in enumerate(word) if mask & (1 << index))
                   for mask in range(1 << len(word)))


class DistinctSubsequenceTests(unittest.TestCase):
    def check(self, source, target, expected):
        result = Solution().numDistinct(source, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_sources_targets_against_position_choice_counts(self):
        sources = [''.join(chars) for size in range(8) for chars in product('ab', repeat=size)]
        targets = [''.join(chars) for size in range(5) for chars in product('ab', repeat=size)]
        checks = 0
        for source in sources:
            counts = counted_position_choices(source)
            for target in targets:
                self.check(source, target, counts[target])
                checks += 1
        self.assertEqual(checks, 7905)

    def test_maximum_lengths_repeated_positions_and_large_intermediate_counts(self):
        self.check('a' * 1000, 'a', 1000)
        self.check('a' * 1000, 'a' * 1000, 1)
        self.check('a' * 1000, 'a' * 999, 1000)
        self.check('b' * 1000, 'a' * 1000, 0)
        self.check('rabbbit', 'rabbit', 3)
        self.check('', '', 1)
        self.check('a', 'aa', 0)


if __name__ == '__main__':
    unittest.main()
