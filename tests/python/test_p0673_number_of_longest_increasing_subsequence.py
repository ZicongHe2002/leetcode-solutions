from itertools import product
import unittest

from python.p0673_number_of_longest_increasing_subsequence import Solution


def every_increasing_index_subset(values):
    longest = count = 0
    for mask in range(1, 1 << len(values)):
        selected = [value for index, value in enumerate(values) if mask >> index & 1]
        if all(selected[index] < selected[index + 1] for index in range(len(selected) - 1)):
            if len(selected) > longest:
                longest, count = len(selected), 1
            elif len(selected) == longest:
                count += 1
    return count


class StrictLongestSubsequenceCountTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = every_increasing_index_subset(values)
        self.assertLessEqual(expected, 2**31 - 1)
        result = Solution().findNumberOfLIS(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_every_increasing_index_subset(self):
        checks = 0
        for size in range(1, 8):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_lengths_duplicate_choices_and_value_endpoints(self):
        self.check(list(range(-1000, 1000)), 1)
        self.check(list(range(1000, -1000, -1)), 2000)
        self.check([7] * 2000, 2000)
        self.check(list(range(1000)) * 2, 1001)
        self.check([value for value in range(30) for _ in range(2)], 2**30)
        self.check([-1000000, 0, 1000000], 1)
        self.check([1, 3, 5, 4, 7], 2)


if __name__ == '__main__':
    unittest.main()
