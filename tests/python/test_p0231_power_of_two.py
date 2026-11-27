import unittest

from python.p0231_power_of_two import Solution


def powers_by_multiplication():
    powers = set()
    value = 1
    while value <= 2147483647:
        powers.add(value)
        value *= 2
    return powers


class PowerOfTwoTests(unittest.TestCase):
    def check(self, value, powers):
        result = Solution().isPowerOfTwo(value)
        self.assertIs(type(result), bool)
        self.assertEqual(result, value in powers)

    def test_all_small_signed_values_against_generated_powers(self):
        powers = powers_by_multiplication()
        for value in range(-1000, 1001):
            self.check(value, powers)

    def test_all_legal_powers_neighbors_and_integer_extremes(self):
        powers = powers_by_multiplication()
        self.assertEqual(len(powers), 31)
        for power in powers:
            for offset in (-1, 0, 1):
                self.check(power + offset, powers)
        for value in (-2147483648, -2147483647, 2147483646, 2147483647):
            self.check(value, powers)


if __name__ == '__main__':
    unittest.main()
