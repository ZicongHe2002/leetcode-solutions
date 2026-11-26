from itertools import product
import unittest

from python.p0306_additive_number import Solution


def all_cut_masks_oracle(text):
    for mask in range(1 << (len(text) - 1)):
        pieces = []
        start = 0
        for boundary in range(1, len(text)):
            if mask & (1 << (boundary - 1)):
                pieces.append(text[start:boundary])
                start = boundary
        pieces.append(text[start:])
        if len(pieces) < 3 or any(len(piece) > 1 and piece[0] == '0' for piece in pieces):
            continue
        values = list(map(int, pieces))
        if all(values[index] == values[index - 1] + values[index - 2] for index in range(2, len(values))):
            return True
    return False


class AdditiveDecimalStringTests(unittest.TestCase):
    def test_all_small_digit_strings_against_full_partition_masks(self):
        strings = 0
        for size in range(1, 8):
            for digits in product('012', repeat=size):
                text = ''.join(digits)
                actual = Solution().isAdditiveNumber(text)
                self.assertIs(type(actual), bool)
                self.assertEqual(actual, all_cut_masks_oracle(text))
                strings += 1
        self.assertEqual(strings, 3279)

    def test_carries_leading_zeroes_and_maximum_digit_count(self):
        for text in ('112358', '199100199', '101', '000', '0' * 35):
            self.assertTrue(Solution().isAdditiveNumber(text))
        for text in ('0', '12', '1023', '9' * 35):
            self.assertFalse(Solution().isAdditiveNumber(text))
        first, second = '1' + '0' * 11, '9' * 11
        text = first + second + str(int(first) + int(second))
        self.assertEqual(len(text), 35)
        self.assertTrue(Solution().isAdditiveNumber(text))
        self.assertTrue(Solution().isAdditiveNumber('999' + '1' + '1000' + '1001' + '2001'))


if __name__ == '__main__':
    unittest.main()
