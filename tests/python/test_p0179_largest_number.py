from itertools import permutations, product
import unittest

from python.p0179_largest_number import Solution


def every_permutation(values):
    best = max(''.join(map(str, order)) for order in permutations(values))
    return best.lstrip('0') or '0'


class LargestConcatenationTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = every_permutation(values)
        result = Solution().largestNumber(values)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_prefix_related_arrays_against_all_permutations(self):
        checks = 0
        for size in range(1, 6):
            for values in product((0, 1, 10, 12, 121), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 3905)

    def test_maximum_length_digit_limit_zero_normalization_and_prefixes(self):
        self.check([10**9] * 100, '1000000000' * 100)
        self.check([0] * 100, '0')
        self.check([9] * 100, '9' * 100)
        self.check([3, 30, 34, 5, 9])
        self.check([121, 12, 1212, 0])


if __name__ == '__main__':
    unittest.main()
