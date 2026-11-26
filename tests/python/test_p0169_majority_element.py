from collections import Counter
from itertools import product
import unittest

from python.p0169_majority_element import Solution


class GuaranteedMajorityTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        counts = Counter(values)
        expected = [value for value, count in counts.items() if count > len(values) // 2]
        self.assertEqual(len(expected), 1)
        result = Solution().majorityElement(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected[0])
        self.assertEqual(values, before)

    def test_all_small_arrays_satisfying_the_majority_promise(self):
        checked = 0
        for size in range(1, 9):
            for values in product((-1, 0, 1), repeat=size):
                counts = Counter(values)
                if max(counts.values()) > size // 2:
                    self.check(list(values))
                    checked += 1
        self.assertGreater(checked, 1000)

    def test_cancellation_reversals_values_and_maximum_size(self):
        self.check([3, 2, 3])
        self.check([2, 2, 1, 1, 1, 2, 2])
        self.check([0])
        self.check([-10**9, 10**9, -10**9])
        self.check([1] * 25001 + [2] * 24999)
        self.check([2] * 20000 + [1] * 30000)
        self.check([0, 1] * 24999 + [0, 0])


if __name__ == '__main__':
    unittest.main()
