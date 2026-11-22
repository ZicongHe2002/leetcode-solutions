import unittest

from python.p0191_number_of_one_bits import Solution


class OneBitTests(unittest.TestCase):
    def check(self, value):
        result = Solution().hammingWeight(value)
        self.assertIs(type(result), int)
        self.assertEqual(result, format(value, 'b').count('1'))

    def test_all_low_words_with_zero_extension_against_binary_text(self):
        for value in range(65536):
            self.check(value)

    def test_original_31_bit_and_explicit_unsigned_32_bit_extensions(self):
        for bit in range(32):
            self.check(1 << bit)
            self.check((1 << bit) - 1)
        for value in [2**31 - 1, 2**32 - 1, 0xAAAAAAAA, 0x55555555, 0]:
            self.check(value)


if __name__ == '__main__':
    unittest.main()
