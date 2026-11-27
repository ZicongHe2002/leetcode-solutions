import random
import unittest
from collections import Counter

from python.p0793_preimage_size_of_factorial_zeroes_function import Solution


def digit_sum(value):
    total = 0
    while value:
        value, digit = divmod(value,5)
        total += digit
    return total


def short_digit_certificate(k):
    bound, digits = 5 * k + 4, 0
    while bound:
        digits += 1
        bound //= 5
    return sum(value - digit_sum(value) == 4 * k
               for value in range(4 * k,4 * k + 4 * digits + 1))


class FactorialZeroPreimageTests(unittest.TestCase):
    def check(self, k, expected):
        result = Solution().preimageSizeFZF(k)
        self.assertIs(type(result),int)
        self.assertEqual(result,expected,k)
        self.assertIn(result,(0,5))

    def test_small_targets_against_literal_factorials_and_decimal_zeroes(self):
        counts = Counter()
        factorial = 1
        for value in range(501):
            if value:
                factorial *= value
            text = str(factorial)
            zeroes = len(text) - len(text.rstrip('0'))
            counts[zeroes] += 1
        self.assertGreater(zeroes,100)
        for k in range(101):
            self.check(k,counts[k])

    def test_large_targets_against_bounded_base_five_digit_certificates(self):
        generator = random.Random(793)
        targets = [generator.randrange(10**9 + 1) for _ in range(1000)]
        targets += [0,1,3,5,10**9 - 1,10**9]
        power = 5
        while power <= 5 * 10**9:
            zeroes = (power - 1) // 4
            targets.extend(k for k in (zeroes - 2,zeroes - 1,zeroes,zeroes + 1) if 0 <= k <= 10**9)
            power *= 5
        for k in targets:
            self.check(k,short_digit_certificate(k))


if __name__ == '__main__':
    unittest.main()
