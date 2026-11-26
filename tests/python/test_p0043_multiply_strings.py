import unittest

from python.p0043_multiply_strings import Solution


class StringMultiplyTests(unittest.TestCase):
    def check(self, first, second):
        result = Solution().multiply(first, second)
        self.assertIs(type(result), str)
        self.assertTrue(result)
        self.assertTrue(all('0' <= digit <= '9' for digit in result))
        self.assertTrue(result == '0' or result[0] != '0')
        self.assertEqual(result, str(int(first) * int(second)))

    def test_every_small_operand_pair_against_integer_multiplication(self):
        checks = 0
        for first in range(101):
            for second in range(101):
                self.check(str(first), str(second))
                checks += 1
        self.assertEqual(checks, 10201)

    def test_maximum_digit_lengths_carry_chains_zero_and_power_of_ten(self):
        self.check('9' * 200, '9' * 200)
        self.check('1' + '0' * 199, '1' + '0' * 199)
        self.check('1234567890' * 20, '9876543210' * 20)
        self.check('0', '9' * 200)
        self.check('9' * 200, '0')
        self.check('1', '9' * 200)


if __name__ == '__main__':
    unittest.main()
