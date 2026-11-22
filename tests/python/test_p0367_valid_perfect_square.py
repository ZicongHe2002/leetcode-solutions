import unittest

from python.p0367_valid_perfect_square import Solution


class IntegerSquareSearchTests(unittest.TestCase):
    def check(self, value, squares):
        result = Solution().isPerfectSquare(value)
        self.assertIs(type(result), bool)
        self.assertEqual(result, value in squares)

    def test_every_small_positive_integer_against_explicit_square_set(self):
        squares = {root * root for root in range(1, 46341)}
        for value in range(1, 10001):
            self.check(value, squares)

    def test_every_signed_32bit_positive_square_and_both_neighbors(self):
        squares = {root * root for root in range(1, 46341)}
        checks = 0
        for root in range(1, 46341):
            square = root * root
            for value in (square - 1, square, square + 1):
                if value >= 1:
                    self.check(value, squares)
                    checks += 1
        self.assertEqual(checks, 139019)
        self.check(2**31 - 1, squares)


if __name__ == '__main__':
    unittest.main()
