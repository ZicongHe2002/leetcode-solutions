from itertools import product
import unittest

from python.p0493_reverse_pairs import Solution


def every_double_inequality_pair(values):
    return sum(values[left] > 2 * values[right]
               for left in range(len(values)) for right in range(left + 1, len(values)))


class DoubledReversePairTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = every_double_inequality_pair(values)
        result = Solution().reversePairs(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_every_small_signed_array_against_all_ordered_index_pairs(self):
        checks = 0
        for size in range(1, 7):
            for values in product((-2, -1, 0, 1, 2), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 19530)

    def test_maximum_lengths_negative_equal_values_and_doubled_32bit_endpoints(self):
        size = 50000
        self.check([-1] * size, size * (size - 1) // 2)
        self.check(list(range(1, size + 1)), 0)
        self.check(list(range(size, 0, -1)), sum((value - 1) // 2 for value in range(1, size + 1)))
        half = 25000
        self.check([2**31 - 1] * half + [-2**31] * half,
                   half * half + half * (half - 1) // 2)
        self.check([-2**31] * half + [2**31 - 1] * half, half * (half - 1) // 2)
        self.check([1, 3, 2, 3, 1], 2)
        self.check([2, 4, 3, 5, 1], 3)


if __name__ == '__main__':
    unittest.main()
