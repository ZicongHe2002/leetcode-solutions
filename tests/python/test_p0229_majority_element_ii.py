from collections import Counter
from itertools import product
import unittest

from python.p0229_majority_element_ii import Solution


class TwoCandidateMajorityTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        frequencies = Counter(values)
        expected = {value for value, count in frequencies.items() if count > len(values) // 3}
        result = Solution().majorityElement(values)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(set(result), expected)
        self.assertLessEqual(len(result), 2)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_full_frequency_count(self):
        arrays = 0
        for size in range(8):
            for values in product((-1, 0, 1, 2), repeat=size):
                self.check(list(values))
                arrays += 1
        self.assertEqual(arrays, 21845)

    def test_strict_threshold_verification_and_maximum_length(self):
        for values in ([], [3, 2, 3], [1, 2], [1, 2, 3], [1, 1, 1, 2, 2, 2, 3, 4, 5], [-10**9] * 4 + [10**9] * 6):
            self.check(values)
        self.check([1] * 16667 + [2] * 16667 + [3] * 16666)
        self.check([1] * 16666 + [2] * 16666 + [3] * 16666 + [4] * 2)


if __name__ == '__main__':
    unittest.main()
