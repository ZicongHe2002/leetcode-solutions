from itertools import product
import unittest

from python.p0492_construct_the_rectangle import Solution


def all_length_factor_oracle(area):
    rectangles = [(length, area // length) for length in range(1, area + 1)
                  if area % length == 0 and length >= area // length]
    return list(min(rectangles, key=lambda pair: pair[0] - pair[1]))


class RectangleFactorGapTests(unittest.TestCase):
    def check(self, area, expected=None):
        result = Solution().constructRectangle(area)
        self.assertIs(type(result), list)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(type(value) is int for value in result))
        length, width = result
        self.assertEqual(length * width, area)
        self.assertGreaterEqual(length, width)
        self.assertEqual(result, all_length_factor_oracle(area) if expected is None else expected)

    def test_every_small_area_against_all_ordered_factor_rectangles(self):
        for area in range(1, 2001):
            self.check(area)

    def test_maximum_area_exact_large_square_and_prime_power_factors(self):
        self.check(10000000, [3200, 3125])
        factors = [2**a * 5**b for a, b in product(range(8), repeat=2)]
        best_width = max(factor for factor in factors if factor * factor <= 10000000)
        self.assertEqual(best_width, 3125)
        self.check(3162**2, [3162, 3162])
        self.check(1 << 23, [4096, 2048])
        self.check(1, [1, 1])
        self.check(37, [37, 1])


if __name__ == '__main__':
    unittest.main()
