import unittest

from python.p0233_number_of_digit_one import Solution


class DigitOnePrefixTests(unittest.TestCase):
    def test_all_small_prefixes_against_decimal_character_counts(self):
        expected = 0
        solver = Solution()
        for upper in range(20001):
            expected += str(upper).count('1')
            result = solver.countDigitOne(upper)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected)

    def test_complete_decimal_blocks_power_boundaries_and_maximum(self):
        solver = Solution()
        self.assertEqual(solver.countDigitOne(0), 0)
        self.assertEqual(solver.countDigitOne(13), 6)
        for exponent in range(1, 10):
            power = 10**exponent
            complete = exponent * 10**(exponent - 1)
            self.assertEqual(solver.countDigitOne(power - 1), complete)
            self.assertEqual(solver.countDigitOne(power), complete + 1)
            if exponent < 9:
                self.assertEqual(solver.countDigitOne(power + 1), complete + 3)
        self.assertEqual(solver.countDigitOne(10**9), 900000001)


if __name__ == '__main__':
    unittest.main()
