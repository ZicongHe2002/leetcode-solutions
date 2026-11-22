import unittest
from itertools import product

from python.p0091_decode_ways import Solution


def cut_mask_oracle(s):
    if not s:
        return 0
    ways = 0
    for mask in range(1 << (len(s) - 1)):
        cuts = [0] + [index + 1 for index in range(len(s) - 1) if mask & (1 << index)] + [len(s)]
        pieces = [s[left:right] for left, right in zip(cuts, cuts[1:])]
        if all(1 <= len(piece) <= 2 and piece[0] != '0' and 1 <= int(piece) <= 26 for piece in pieces):
            ways += 1
    return ways


class DecodeTests(unittest.TestCase):
    def test_all_small_digit_strings_against_cut_masks(self):
        checks = 0
        for size in range(7):
            for digits in product('0123', repeat=size):
                text = ''.join(digits)
                self.assertEqual(Solution().numDecodings(text), cut_mask_oracle(text))
                checks += 1
        self.assertEqual(checks, 5461)

    def test_zero_rules_examples_and_maximum_length_within_integer_contract(self):
        for text, expected in [('', 0), ('06', 0), ('10', 1), ('20', 1), ('26', 2), ('27', 1),
                               ('100', 0), ('11106', 2), ('226', 3), ('10' * 50, 1),
                               ('9' * 100, 1), ('0' + '1' * 99, 0)]:
            self.assertEqual(Solution().numDecodings(text), expected)


if __name__ == '__main__':
    unittest.main()
