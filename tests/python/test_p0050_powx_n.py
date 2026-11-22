import math
import unittest

from python.p0050_powx_n import Solution


class PowerTests(unittest.TestCase):
    def check(self, base, exponent):
        expected = pow(base, exponent)
        self.assertLessEqual(abs(expected), 10000)
        result = Solution().myPow(base, exponent)
        self.assertIs(type(result), float)
        self.assertTrue(math.isclose(result, expected, rel_tol=1e-6, abs_tol=1e-9),
                        (base, exponent, result, expected))

    def test_small_signed_exponents_against_builtin_power(self):
        checks = 0
        for base in (-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0):
            for exponent in range(-8, 9):
                if base == 0 and exponent <= 0:
                    continue
                self.check(base, exponent)
                checks += 1
        self.assertEqual(checks, 110)

    def test_extreme_exponents_near_one_large_base_and_underflow(self):
        for base in (-1.0, 1.0):
            for exponent in (-2**31, 2**31 - 1):
                self.check(base, exponent)
        self.check(2.0, -2**31)
        self.check(0.5, 2**31 - 1)
        self.check(99.999, 2)
        self.check(1.0000000001, 2**31 - 1)
        self.check(1.001, -4096)
        self.check(0.0, 2**31 - 1)


if __name__ == '__main__':
    unittest.main()
