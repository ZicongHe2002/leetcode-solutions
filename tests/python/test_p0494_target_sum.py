import unittest
from collections import Counter
from itertools import product
from math import comb

from python.p0494_target_sum import Solution


class TargetSumTests(unittest.TestCase):
    def check(self, values, target, expected):
        before = values[:]
        result = Solution().findTargetSumWays(values, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_and_targets_against_explicit_sign_assignments(self):
        arrays = checks = 0
        for size in range(1, 7):
            for values in product(range(3), repeat=size):
                frequencies = Counter(sum(sign * value for sign, value in zip(signs, values))
                                      for signs in product((-1, 1), repeat=size))
                arrays += 1
                for target in range(-6, 7):
                    self.check(list(values), target, frequencies[target])
                    checks += 1
        self.assertEqual((arrays, checks), (1092, 14196))

    def test_maximum_zeros_total_parity_and_target_extremes(self):
        self.check([0] * 20, 0, 2**20)
        for target in [-1000, 1000]:
            self.check([1000] + [0] * 19, target, 2**19)
        self.check([50] * 20, 0, comb(20, 10))
        self.check([1] * 19 + [0], 0, 0)
        self.check([1], 1000, 0)


if __name__ == '__main__':
    unittest.main()
