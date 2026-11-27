import unittest

from python.p0201_bitwise_and_of_numbers_range import Solution


def direct_interval_and(left, right):
    result = left
    for value in range(left, right + 1):
        result &= value
    return result


class CommonPrefixRangeAndTests(unittest.TestCase):
    def check(self, left, right, expected=None):
        if expected is None:
            expected = direct_interval_and(left, right)
        result = Solution().rangeBitwiseAnd(left, right)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_closed_intervals_against_direct_and(self):
        checks = 0
        for left in range(128):
            for right in range(left, 128):
                self.check(left, right)
                checks += 1
        self.assertEqual(checks, 8256)

    def test_each_bit_boundary_large_ranges_and_equal_endpoints(self):
        maximum = 2**31 - 1
        for bit in range(31):
            boundary = 1 << bit
            for left in range(max(0, boundary - 3), boundary + 1):
                for right in range(boundary, min(maximum, boundary + 3) + 1):
                    self.check(left, right)
        self.check(0, maximum, 0)
        self.check(1 << 30, maximum, 1 << 30)
        self.check(maximum, maximum, maximum)
        self.check(maximum - 1, maximum, maximum - 1)


if __name__ == '__main__':
    unittest.main()
