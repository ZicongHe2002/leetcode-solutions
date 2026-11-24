import unittest
from itertools import product

from python.p1493_longest_subarray_after_deleting_one_element import Solution


def explicit_deletions(values):
    best = 0
    for deleted in range(len(values)):
        remaining = values[:deleted] + values[deleted + 1:]
        best = max(best, max(map(len, ''.join(map(str, remaining)).split('0'))))
    return best


class DeleteWindowTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = explicit_deletions(values)
        result = Solution().longestSubarray(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_binary_arrays_against_real_deletions(self):
        checks = 0
        for size in range(13):
            for values in product((0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 8191)

    def test_maximum_lengths_exact_deletion_and_adjacent_zeros(self):
        self.check([1] * 100000, 99999)
        self.check([0] * 100000, 0)
        self.check([0, 1] * 50000, 2)
        self.check([1] * 49999 + [0] + [1] * 50000, 99999)
        self.check([1] * 49999 + [0, 0] + [1] * 49999, 49999)


if __name__ == '__main__':
    unittest.main()
