import unittest
from math import isqrt

from python.p0069_sqrtx import Solution


class IntegerSquareRootTests(unittest.TestCase):
    def check(self, value):
        result = Solution().mySqrt(value)
        self.assertIs(type(result), int)
        self.assertEqual(result, isqrt(value))
        self.assertLessEqual(result * result, value)
        self.assertGreater((result + 1) * (result + 1), value)

    def test_every_small_integer_against_isqrt_and_square_inequalities(self):
        for value in range(10001):
            self.check(value)

    def test_perfect_square_neighbors_and_maximum_32_bit_value(self):
        for root in (1, 2, 3, 100, 10000, 46340):
            for value in (root * root - 1, root * root, root * root + 1):
                self.check(value)
        self.check(2**31 - 1)
        self.check(2**31 - 2)
        self.check(2147395599)


if __name__ == '__main__':
    unittest.main()
