import unittest

from python.p0693_binary_number_with_alternating_bits import Solution


def alternating_text_reference(value):
    text = format(value, 'b')
    return all(text[index] != text[index + 1] for index in range(len(text) - 1))


class AdjacentDifferenceAllOnesTests(unittest.TestCase):
    def check(self, value):
        result = Solution().hasAlternatingBits(value)
        self.assertIs(type(result), bool)
        self.assertEqual(result, alternating_text_reference(value))

    def test_every_positive_16bit_value_against_adjacent_text_characters(self):
        for value in range(1, 65536):
            self.check(value)

    def test_every_width_alternation_single_flips_and_extreme_patterns(self):
        for width in range(1, 32):
            alternating = int(('10' * 16)[:width], 2)
            self.check(alternating)
            self.check((1 << width) - 1)
            self.check(1 << (width - 1))
            for bit in range(width):
                changed = alternating ^ (1 << bit)
                if changed:
                    self.check(changed)


if __name__ == '__main__':
    unittest.main()
