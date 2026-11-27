import unittest

from python.p0326_power_of_three import Solution


def generated_powers():
    powers = set()
    value = 1
    while value <= 2**31 - 1:
        powers.add(value)
        value *= 3
    return powers


class BoundedPowerOfThreeTests(unittest.TestCase):
    def check(self, value, powers):
        result = Solution().isPowerOfThree(value)
        self.assertIs(type(result), bool)
        self.assertEqual(result, value in powers)

    def test_all_small_signed_values_against_generated_power_set(self):
        powers = generated_powers()
        self.assertEqual(len(powers), 20)
        for value in range(-1000, 10001):
            self.check(value, powers)

    def test_every_power_neighbors_and_signed_32bit_endpoints(self):
        powers = generated_powers()
        for power in powers:
            for value in (power - 1, power, power + 1):
                self.check(value, powers)
        for value in (-2**31, -2**31 + 1, 2**31 - 2, 2**31 - 1, 3**19):
            self.check(value, powers)


if __name__ == '__main__':
    unittest.main()
