from itertools import product
import unittest

from python.p0717_one_bit_and_two_bit_characters import Solution


def all_complete_codeword_streams(limit):
    endings = {}

    def visit(bits, last_single):
        if bits and bits[-1] == 0:
            if bits in endings:
                assert endings[bits] == last_single
            endings[bits] = last_single
        for token in ((0,), (1, 0), (1, 1)):
            combined = bits + token
            if len(combined) <= limit:
                visit(combined, len(token) == 1)

    visit((), False)
    return endings


class LastCodewordBoundaryTests(unittest.TestCase):
    def check(self, bits, expected):
        before = bits[:]
        result = Solution().isOneBitCharacter(bits)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(bits, before)

    def test_all_small_zero_terminated_arrays_against_generated_codeword_streams(self):
        endings = all_complete_codeword_streams(12)
        checks = 0
        for size in range(1, 13):
            for prefix in product((0, 1), repeat=size - 1):
                bits = prefix + (0,)
                self.check(list(bits), endings[bits])
                checks += 1
        self.assertEqual((len(endings), checks), (4095, 4095))

    def test_maximum_length_ones_parity_and_repeated_two_bit_codes(self):
        self.check([0] * 1000, True)
        self.check([1] * 999 + [0], False)
        self.check([1] * 998 + [0, 0], True)
        self.check([1, 0] * 500, False)
        self.check([1, 1] * 499 + [0, 0], True)
        self.check([1, 0, 0], True)
        self.check([1, 1, 1, 0], False)


if __name__ == '__main__':
    unittest.main()
