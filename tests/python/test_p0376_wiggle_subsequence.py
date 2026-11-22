from itertools import product
import unittest

from python.p0376_wiggle_subsequence import Solution


def all_subsequences(values):
    best = 0
    for mask in range(1 << len(values)):
        candidate = [value for index, value in enumerate(values) if mask >> index & 1]
        differences = [right - left for left, right in zip(candidate, candidate[1:])]
        if all(differences) and all(first * second < 0
                                    for first, second in zip(differences, differences[1:])):
            best = max(best, len(candidate))
    return best


class WiggleSubsequenceGreedyTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = all_subsequences(values)
        result = Solution().wiggleMaxLength(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_all_ordered_subsequences(self):
        checks = 0
        for size in range(1, 8):
            for values in product((0, 1, 2), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_length_equal_monotonic_alternating_and_plateaus(self):
        self.check([1000] * 1000, 1)
        self.check(list(range(1000)), 2)
        self.check([0, 1000] * 500, 1000)
        self.check([0] * 499 + [1000] * 501, 2)
        self.check([1, 7, 4, 9, 2, 5], 6)


if __name__ == '__main__':
    unittest.main()
