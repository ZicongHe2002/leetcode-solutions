from itertools import product
import unittest

from python.p0315_count_of_smaller_numbers_after_self import Solution


def direct_suffix_comparison(values):
    return [sum(other < value for other in values[index + 1:])
            for index, value in enumerate(values)]


class StrictSmallerSuffixCountTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = direct_suffix_comparison(values)
        result = Solution().countSmaller(values)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(count) is int for count in result))
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_direct_suffix_comparisons(self):
        checks = 0
        for size in range(1, 9):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_repeated_values_extremes_and_descending_blocks(self):
        self.check([-10000] * 100000, [0] * 100000)
        self.check([10000] * 50000 + [-10000] * 50000, [50000] * 50000 + [0] * 50000)
        values = list(range(10000, -10000, -1)) * 5
        expected = [(5 - index // 20000) * (19999 - index % 20000) for index in range(100000)]
        self.check(values, expected)
        self.check([5, 2, 6, 1], [2, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
