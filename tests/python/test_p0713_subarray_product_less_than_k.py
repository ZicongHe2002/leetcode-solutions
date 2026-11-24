import unittest
from itertools import product

from python.p0713_subarray_product_less_than_k import Solution


def all_interval_products(values, threshold):
    result = 0
    for start in range(len(values)):
        value = 1
        for end in range(start, len(values)):
            value *= values[end]
            result += value < threshold
    return result


class ProductWindowTests(unittest.TestCase):
    def check(self, values, threshold, expected=None):
        before = values[:]
        if expected is None:
            expected = all_interval_products(values, threshold)
        result = Solution().numSubarrayProductLessThanK(values, threshold)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_positive_arrays_and_strict_thresholds_against_products(self):
        arrays = checks = 0
        for size in range(7):
            for values in product(range(1, 5), repeat=size):
                arrays += 1
                for threshold in (0, 1, 2, 3, 5, 10, 20, 100, 1000000):
                    self.check(list(values), threshold)
                    checks += 1
        self.assertEqual((arrays, checks), (5461, 49149))

    def test_maximum_length_and_equality_exclusion(self):
        self.check([1] * 30000, 2, 450015000)
        self.check([1] * 30000, 1, 0)
        self.check([1000] * 30000, 1000000, 30000)
        self.check([2] * 30000, 1024, 9 * 30000 - 36)
        self.check([10, 5, 2, 6], 100, 8)


if __name__ == '__main__':
    unittest.main()
