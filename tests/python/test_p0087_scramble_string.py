import unittest
from functools import lru_cache
from itertools import product

from python.p0087_scramble_string import Solution


@lru_cache(None)
def reachable(text):
    result = {text}
    for split in range(1, len(text)):
        for first in reachable(text[:split]):
            for second in reachable(text[split:]):
                result.add(first + second)
                result.add(second + first)
    return frozenset(result)


class ScrambleStringTests(unittest.TestCase):
    def test_all_small_ternary_pairs_against_constructed_language(self):
        queries = 0
        solver = Solution()
        for size in range(6):
            strings = [''.join(chars) for chars in product('abc', repeat=size)]
            for source in strings:
                expected = reachable(source)
                for target in strings:
                    self.assertIs(solver.isScramble(source, target), target in expected,
                                  (source, target))
                    queries += 1
        self.assertEqual(queries, 66430)

    def test_examples_maximum_length_and_declared_extensions(self):
        solver = Solution()
        self.assertIs(solver.isScramble('great', 'rgeat'), True)
        self.assertIs(solver.isScramble('abcde', 'caebd'), False)
        self.assertIs(solver.isScramble('a', 'a'), True)
        self.assertIs(solver.isScramble('a', 'b'), False)
        source = 'abcdefghijklmnopqrstuvwxyzabcd'
        self.assertEqual(len(source), 30)
        for target in (source, source[::-1], source[11:] + source[:11]):
            self.assertIs(solver.isScramble(source, target), True)
        self.assertIs(solver.isScramble('a' * 30, 'a' * 29 + 'b'), False)
        self.assertIs(solver.isScramble('', ''), True)
        self.assertIs(solver.isScramble('a', ''), False)
        self.assertIs(solver.isScramble('', 'a'), False)


if __name__ == '__main__':
    unittest.main()
