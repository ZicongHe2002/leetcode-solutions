import unittest

from python.p0067_add_binary import Solution


class BinaryAdditionTests(unittest.TestCase):
    def check(self, first, second):
        result = Solution().addBinary(first, second)
        self.assertIs(type(result), str)
        self.assertTrue(result)
        self.assertTrue(all(bit in '01' for bit in result))
        self.assertTrue(result == '0' or result[0] != '0')
        self.assertEqual(result, format(int(first, 2) + int(second, 2), 'b'))

    def test_every_small_binary_operand_pair_against_integer_sum(self):
        checks = 0
        for first in range(64):
            for second in range(64):
                self.check(format(first, 'b'), format(second, 'b'))
                checks += 1
        self.assertEqual(checks, 4096)

    def test_maximum_lengths_full_carry_alternating_bits_and_zero(self):
        self.check('1' * 10000, '1')
        self.assertEqual(Solution().addBinary('1' * 10000, '1'), '1' + '0' * 10000)
        self.check('10' * 5000, '1' * 10000)
        self.check('0', '1' * 10000)
        self.check('1' * 10000, '0')
        self.check('0', '0')


if __name__ == '__main__':
    unittest.main()
