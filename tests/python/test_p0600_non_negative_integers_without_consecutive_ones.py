from math import comb
import unittest

from python.p0600_non_negative_integers_without_consecutive_ones import Solution


def nonadjacent_position_choices(width):
    return sum(comb(width - ones + 1, ones) for ones in range((width + 1) // 2 + 1))


class NoAdjacentOnesTests(unittest.TestCase):
    def check(self, n, expected):
        result = Solution().findIntegers(n)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, n)

    def test_every_small_upper_bound_against_binary_string_enumeration(self):
        total = 0
        for n in range(100001):
            total += '11' not in bin(n)
            self.check(n, total)

    def test_large_bit_boundaries_against_nonadjacent_position_combinations(self):
        for width in range(1, 31):
            all_ones = (1 << width) - 1
            if all_ones <= 10**9:
                self.check(all_ones, nonadjacent_position_choices(width))
            power = 1 << width
            if power <= 10**9:
                self.check(power, nonadjacent_position_choices(width) + 1)
            leading_pair = 3 << (width - 1)
            if leading_pair <= 10**9:
                self.check(leading_pair, nonadjacent_position_choices(width + 1))
        largest_valid_thirty_bit = int('10' * 15, 2)
        self.assertLess(largest_valid_thirty_bit, 10**9)
        self.assertEqual(nonadjacent_position_choices(30), 2178309)
        self.check(largest_valid_thirty_bit, 2178309)
        self.check(10**9, 2178309)
        self.check(0, 1)
        self.check(5, 5)


if __name__ == '__main__':
    unittest.main()
