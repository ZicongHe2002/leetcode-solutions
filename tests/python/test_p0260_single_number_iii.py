from collections import Counter
from itertools import product
import random
import unittest

from python.p0260_single_number_iii import Solution


class TwoSingletonPartitionTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        counts = Counter(values)
        self.assertEqual(sorted(counts.values()), [1, 1] + [2] * (len(counts) - 2))
        expected = {value for value, count in counts.items() if count == 1}
        result = Solution().singleNumber(values)
        self.assertIs(type(result), list)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(set(result), expected)
        self.assertEqual(values, before)

    def test_all_small_legal_arrays_against_counter(self):
        checks = 0
        for size in (2, 4, 6):
            for values in product((-1, 0, 1, 2), repeat=size):
                counts = Counter(values)
                if sorted(counts.values()) == [1, 1] + [2] * (len(counts) - 2):
                    self.check(list(values))
                    checks += 1
        self.assertEqual(checks, 1236)

    def test_maximum_length_sign_bit_and_integer_extremes(self):
        values = [-2147483648, 2147483647] + [value for value in range(-7499, 7500)
                                               for _ in range(2)]
        self.assertEqual(len(values), 30000)
        random.Random(260).shuffle(values)
        self.check(values)
        self.check([-1, 0])
        self.check([-2147483648, 0])
        self.check([-2147483648, -2147483647, 2147483647, 2147483647])
        self.check([-2147483648, 1, 2147483647, 1])
        self.check([1, 2, 1, 3, 2, 5])


if __name__ == '__main__':
    unittest.main()
