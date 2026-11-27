from collections import Counter
from itertools import product
import unittest

from python.p0041_first_missing_positive import Solution


def positive_set_oracle(values):
    present = {value for value in values if value > 0}
    answer = 1
    while answer in present:
        answer += 1
    return answer


class FirstMissingPositiveTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        expected = positive_set_oracle(before) if expected is None else expected
        result = Solution().firstMissingPositive(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(Counter(values), Counter(before))

    def test_all_small_arrays_against_positive_set(self):
        arrays = 0
        for size in range(7):
            for values in product((-1, 0, 1, 2, 3, 4), repeat=size):
                self.check(list(values))
                arrays += 1
        self.assertEqual(arrays, 55987)

    def test_duplicate_cycles_large_permutations_and_numeric_boundaries(self):
        self.check([3, 4, -1, 1], 2)
        self.check([1, 1], 2)
        self.check([2, 2], 1)
        self.check(list(range(100000, 0, -1)), 100001)
        self.check([1] * 100000, 2)
        self.check([100001] * 100000, 1)
        self.check([-2**31, 2**31 - 1, 1, 2], 3)
        solver = Solution()
        self.assertEqual(solver.firstMissingPositive([2, 1]), 3)
        self.assertEqual(solver.firstMissingPositive([]), 1)


if __name__ == '__main__':
    unittest.main()
