import unittest

from python.p0343_integer_break import Solution


def every_separator_mask_product(total):
    best = 0
    for mask in range(1, 1 << (total - 1)):
        product = 1
        previous = 0
        for cut in range(1, total):
            if mask >> (cut - 1) & 1:
                product *= cut - previous
                previous = cut
        product *= total - previous
        best = max(best, product)
    return best


def first_part_dynamic_reference(limit):
    best = [0] * (limit + 1)
    for total in range(2, limit + 1):
        best[total] = max(first * max(total - first, best[total - first])
                          for first in range(1, total))
    return best


class IntegerBreakPartitionTests(unittest.TestCase):
    def check(self, total, expected):
        result = Solution().integerBreak(total)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_every_small_ordered_split_via_nonempty_separator_masks(self):
        for total in range(2, 13):
            self.check(total, every_separator_mask_product(total))
        self.assertEqual(sum((1 << (total - 1)) - 1 for total in range(2, 13)), 4083)

    def test_every_legal_total_against_full_first_part_dynamic_reference(self):
        reference = first_part_dynamic_reference(58)
        for total in range(2, 59):
            self.check(total, reference[total])
        self.check(2, 1)
        self.check(3, 2)
        self.check(4, 4)
        self.check(58, 1549681956)


if __name__ == '__main__':
    unittest.main()
