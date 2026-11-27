import random
import unittest
from bisect import bisect_right
from itertools import combinations_with_replacement

from python.p0738_monotone_increasing_digits import Solution


ALL_VALID = [0] + [int(''.join(digits)) for size in range(1, 10)
                   for digits in combinations_with_replacement('123456789', size)]


class MonotoneDigitsTests(unittest.TestCase):
    def check(self, n, expected=None):
        result = Solution().monotoneIncreasingDigits(n)
        self.assertIs(type(result), int)
        self.assertEqual(result, ALL_VALID[bisect_right(ALL_VALID, n) - 1] if expected is None else expected, n)

    def test_every_valid_number_and_immediately_preceding_input_against_complete_candidate_set(self):
        self.assertEqual(len(ALL_VALID), 48620)
        self.assertEqual(ALL_VALID, sorted(set(ALL_VALID)))
        checked = 0
        for index, value in enumerate(ALL_VALID):
            self.check(value, value)
            checked += 1
            if index:
                self.check(value - 1, ALL_VALID[index - 1])
                checked += 1
        self.assertEqual(checked, 97239)

    def test_seeded_full_domain_queries_and_cascading_borrow_edges(self):
        rng = random.Random(738)
        for _ in range(1000):
            self.check(rng.randrange(10**9 + 1))
        for value, expected in ((0,0),(10,9),(1234,1234),(332,299),(1000,999),
                                 (120,119),(111110,99999),(10**9,999999999)):
            self.check(value, expected)


if __name__ == '__main__':
    unittest.main()
