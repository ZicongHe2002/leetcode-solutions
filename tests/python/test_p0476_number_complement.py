import unittest

from python.p0476_number_complement import Solution


def literal_binary_flip(value):
    return int(''.join('1' if bit == '0' else '0' for bit in format(value, 'b')), 2)


class SignificantWidthComplementTests(unittest.TestCase):
    def check(self, value):
        result = Solution().findComplement(value)
        self.assertIs(type(result), int)
        self.assertEqual(result, literal_binary_flip(value))

    def test_every_small_positive_value_against_literal_text_flip(self):
        for value in range(1, 10001):
            self.check(value)

    def test_every_legal_width_single_top_bit_all_ones_and_alternation(self):
        for width in range(1, 32):
            self.check(1 << (width - 1))
            self.check((1 << width) - 1)
            self.check(int(('10' * 16)[:width], 2))
        self.check(5)
        self.check(1)


if __name__ == '__main__':
    unittest.main()
