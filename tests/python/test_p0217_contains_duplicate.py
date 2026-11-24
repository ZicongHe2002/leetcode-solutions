import unittest
from itertools import product

from python.p0217_contains_duplicate import Solution


class SolutionTests(unittest.TestCase):
    def check(self, values, expected, *args):
        before = values[:]
        actual = Solution().containsDuplicate(values, *args)
        self.assertEqual(actual, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_index_pairs(self):
        checked = 0
        for size in range(7):
            for values in product(range(-2, 3), repeat=size):
                expected = any(values[i] == values[j] for i in range(size) for j in range(i + 1, size))
                self.check(list(values), expected)
                checked += 1
        self.assertEqual(checked, 19531)

    def test_length_value_boundaries_and_late_duplicate(self):
        self.check(list(range(100000)), False)
        self.check(list(range(99999)) + [0], True)
        self.check([-10**9, 10**9], False)
        self.check([10**9, 10**9], True)
        self.check([0], False)

if __name__ == '__main__':
    unittest.main()
