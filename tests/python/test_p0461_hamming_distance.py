import unittest

from python.p0461_hamming_distance import Solution


def fixed_width_text_distance(left, right):
    return sum(a != b for a, b in zip(format(left, '031b'), format(right, '031b')))


class DifferingBitRemovalTests(unittest.TestCase):
    def check(self, left, right):
        result = Solution().hammingDistance(left, right)
        self.assertIs(type(result), int)
        self.assertEqual(result, fixed_width_text_distance(left, right))

    def test_all_small_pairs_against_padded_binary_text(self):
        for left in range(128):
            for right in range(128):
                self.check(left, right)

    def test_every_bit_and_complement_mask_at_full_width(self):
        maximum = 2**31 - 1
        values = {0, maximum, int('10' * 15 + '1', 2), int('01' * 15 + '0', 2)}
        for bit in range(31):
            values.add(1 << bit)
            values.add(maximum ^ (1 << bit))
        for left in values:
            for right in values:
                self.check(left, right)
        self.check(1, 4)
        self.check(3, 1)


if __name__ == '__main__':
    unittest.main()
