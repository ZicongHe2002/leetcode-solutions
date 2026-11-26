import unittest
from itertools import product

from python.p0639_decode_ways_ii import Solution


MODULUS = 10**9 + 7


def expanded_partitions(text):
    def partitions(digits):
        if not digits:
            return 1
        if digits[0] == '0':
            return 0
        count = partitions(digits[1:])
        if len(digits) >= 2 and 10 <= int(digits[:2]) <= 26:
            count += partitions(digits[2:])
        return count
    choices = ['123456789' if char == '*' else char for char in text]
    return sum(partitions(''.join(digits)) for digits in product(*choices))


def all_star_tilings(length):
    factorial = [1] * (length + 1)
    for value in range(1, length + 1):
        factorial[value] = factorial[value - 1] * value % MODULUS
    inverse = [1] * (length + 1)
    inverse[length] = pow(factorial[length], MODULUS - 2, MODULUS)
    for value in range(length, 0, -1):
        inverse[value - 1] = inverse[value] * value % MODULUS
    answer = 0
    pairs_weight, singles_weight = 1, pow(9, length, MODULUS)
    remove_two_singles = pow(81, MODULUS - 2, MODULUS)
    for pairs in range(length // 2 + 1):
        placements = factorial[length - pairs] * inverse[pairs] % MODULUS
        placements = placements * inverse[length - 2 * pairs] % MODULUS
        answer = (answer + placements * pairs_weight * singles_weight) % MODULUS
        pairs_weight = pairs_weight * 15 % MODULUS
        singles_weight = singles_weight * remove_two_singles % MODULUS
    return answer


class WildcardDecodingTests(unittest.TestCase):
    def check(self, text, expected):
        actual = Solution().numDecodings(text)
        self.assertIs(type(actual), int)
        self.assertGreaterEqual(actual, 0)
        self.assertLess(actual, MODULUS)
        self.assertEqual(actual, expected % MODULUS, text if len(text) < 10 else None)

    def test_all_short_strings_against_expansion_and_actual_partitions(self):
        checks = 0
        for alphabet, lengths in (('0123456789*', range(1, 4)), ('0126*', range(4, 6))):
            for size in lengths:
                for characters in product(alphabet, repeat=size):
                    text = ''.join(characters)
                    self.check(text, expanded_partitions(text))
                    checks += 1
        self.assertEqual(checks, 5213)

    def test_maximum_lengths_combinatorial_star_count_and_zero_boundaries(self):
        self.check('*' * 100000, all_star_tilings(100000))
        self.check('0' * 100000, 0)
        self.check('10' * 50000, 1)
        self.check('*0' * 50000, pow(2, 50000, MODULUS))
        self.check('30' + '*' * 99998, 0)


if __name__ == '__main__':
    unittest.main()
