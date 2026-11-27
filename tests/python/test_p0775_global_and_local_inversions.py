import unittest
from itertools import permutations

from python.p0775_global_and_local_inversions import Solution


def literal_global_and_local_counts(values):
    global_count = sum(values[left] > values[right] for left in range(len(values))
                       for right in range(left + 1, len(values)))
    local_count = sum(left > right for left, right in zip(values, values[1:]))
    return global_count == local_count


class GlobalLocalInversionsTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        result = Solution().isIdealPermutation(values)
        self.assertIs(type(result), bool)
        self.assertEqual(result, literal_global_and_local_counts(values) if expected is None else expected, values[:20])
        self.assertEqual(values, before)

    def test_every_small_permutation_against_independently_counted_global_and_local_pairs(self):
        checked = 0
        for size in range(1, 9):
            for values in permutations(range(size)):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 46233)

    def test_official_examples_maximum_length_adjacent_swaps_and_nonlocal_cycles(self):
        self.check([1,0,2], True)
        self.check([1,2,0], False)
        self.check([0], True)
        self.check([1,0], True)
        self.check(list(range(100000)), True)
        self.check([index ^ 1 for index in range(100000)], True)
        self.check(list(reversed(range(100000))), False)
        self.check([2,0,1] + list(range(3, 100000)), False)


if __name__ == '__main__':
    unittest.main()
