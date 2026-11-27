from collections import Counter
from itertools import product
import random
import unittest

from python.p0137_single_number_ii import Solution


class ModuloThreeStateTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        counts = Counter(values)
        self.assertEqual(sorted(counts.values()), [1] + [3] * (len(counts) - 1))
        expected = next(value for value, count in counts.items() if count == 1)
        result = Solution().singleNumber(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_legal_arrays_against_counter(self):
        checks = 0
        for size in (1, 4, 7):
            for values in product((-1, 0, 1), repeat=size):
                counts = Counter(values)
                if sorted(counts.values()) == [1] + [3] * (len(counts) - 1):
                    self.check(list(values))
                    checks += 1
        self.assertEqual(checks, 447)

    def test_largest_legal_length_negative_sign_and_value_extremes(self):
        values = [-2147483648] + [value for value in range(-4999, 5000)
                                  for _ in range(3)]
        self.assertEqual(len(values), 29998)
        random.Random(137).shuffle(values)
        self.check(values)
        self.check([2147483647] + [-2147483648] * 3 + [-1] * 3 + [0] * 3)
        self.check([-2147483648])
        self.check([2147483647])
        self.check([0])
        self.check([0, 1, 0, 1, 0, 1, 99])


if __name__ == '__main__':
    unittest.main()
