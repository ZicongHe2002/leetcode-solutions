import unittest

from python.p0372_super_pow import Solution


class DecimalExponentFoldTests(unittest.TestCase):
    def check(self, a, digits, expected):
        before = digits[:]
        actual = Solution().superPow(a, digits)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected)
        self.assertGreaterEqual(actual, 0)
        self.assertLess(actual, 1337)
        self.assertEqual(digits, before)

    def test_small_exponents_against_repeated_modular_multiplication(self):
        queries = 0
        for a in (1, 2, 7, 191, 1337, 2**31 - 1):
            expected = 1
            for exponent in range(501):
                self.check(a, [int(char) for char in str(exponent)], expected)
                expected = expected * a % 1337
                queries += 1
        self.assertEqual(queries, 3006)

    def test_maximum_exponent_length_non_coprime_bases_and_zero_digits(self):
        digits = [9] * 2000
        exponent = int('9' * 2000)
        for a in (2, 7, 191, 1337, 2**31 - 1):
            self.check(a, digits[:], pow(a, exponent, 1337))
        self.check(2, [1, 0], 1024)
        self.check(2, [1, 0, 0, 0], pow(2, 1000, 1337))
        self.check(1337, [0], 1)
        self.check(1, [1] + [0] * 1999, 1)


if __name__ == '__main__':
    unittest.main()
