import unittest

from python.p0405_convert_number_to_hexadecimal import Solution


class HexadecimalSignedBytesOracleTests(unittest.TestCase):
    def check(self, number):
        expected = number.to_bytes(4, 'big', signed=True).hex().lstrip('0') or '0'
        result = Solution().toHex(number)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertTrue(result and all(character in '0123456789abcdef' for character in result))
        self.assertLessEqual(len(result), 8)
        self.assertTrue(result == '0' or not result.startswith('0'))
        decoded = int(result, 16)
        if decoded >= 2**31:
            decoded -= 2**32
        self.assertEqual(decoded, number)

    def test_all_small_signed_integers_against_fixed_width_signed_bytes(self):
        for number in range(-10000, 10001):
            self.check(number)

    def test_int32_endpoints_and_hex_digit_carries(self):
        for number in (-2**31, -2**31 + 1, -16, -1, 0, 1, 15, 16, 2**31 - 2, 2**31 - 1):
            self.check(number)


if __name__ == '__main__':
    unittest.main()
