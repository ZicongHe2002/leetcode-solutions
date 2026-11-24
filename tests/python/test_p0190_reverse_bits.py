import unittest

from python.p0190_reverse_bits import Solution


class ReverseBitTests(unittest.TestCase):
    def check(self, value):
        expected = int(format(value, '032b')[::-1], 2)
        result = Solution().reverseBits(value)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 2**32)

    def test_all_low_words_split_between_original_even_domain_and_odd_extensions(self):
        for value in range(65536):
            self.check(value)

    def test_original_maximum_even_and_explicit_unsigned_32_bit_extensions(self):
        for bit in range(32):
            self.check(1 << bit)
            self.check((1 << bit) - 1)
        for value in [0, 2**31 - 2, 2**32 - 1, 2**32 - 2, 0xAAAAAAAA, 0x55555555]:
            self.check(value)


if __name__ == '__main__':
    unittest.main()
