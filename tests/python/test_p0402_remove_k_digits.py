import unittest
from itertools import combinations, product

from python.p0402_remove_k_digits import Solution


def all_retained_positions(number, removed):
    candidates = (''.join(number[index] for index in indices)
                  for indices in combinations(range(len(number)), len(number) - removed))
    return str(min(int(candidate) if candidate else 0 for candidate in candidates))


class RemoveDigitTests(unittest.TestCase):
    def check(self, number, removed, expected=None):
        if expected is None:
            expected = all_retained_positions(number, removed)
        result = Solution().removeKdigits(number, removed)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)

    def test_small_valid_numbers_and_removal_counts_against_all_positions(self):
        numbers = checks = 0
        for size in range(1, 7):
            for digits in product('0123', repeat=size):
                if size > 1 and digits[0] == '0':
                    continue
                number = ''.join(digits)
                numbers += 1
                for removed in range(size + 1):
                    self.check(number, removed)
                    checks += 1
        self.assertEqual((numbers, checks), (4096, 27308))

    def test_maximum_length_leading_zero_normalization_and_leftover_removals(self):
        self.check('9' * 100000, 50000, '9' * 50000)
        self.check('1' + '0' * 99999, 1, '0')
        self.check('123456789' * 11111 + '1', 99999, '1')
        self.check('9' * 100000, 100000, '0')
        self.check('123456789', 4, '12345')
        self.check('987654321', 4, '54321')
        self.check('10200', 0, '10200')


if __name__ == '__main__':
    unittest.main()
