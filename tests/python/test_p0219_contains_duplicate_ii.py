from itertools import product
import unittest

from python.p0219_contains_duplicate_ii import Solution


def all_pairs_oracle(values, distance):
    return any(values[left] == values[right] and right - left <= distance
               for left in range(len(values)) for right in range(left + 1, len(values)))


class NearbyDuplicateTests(unittest.TestCase):
    def check(self, values, distance, expected=None):
        before = values[:]
        expected = all_pairs_oracle(values, distance) if expected is None else expected
        result = Solution().containsNearbyDuplicate(values, distance)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_and_distances_against_all_pairs(self):
        arrays = 0
        for size in range(8):
            for values in product((-1, 0, 1), repeat=size):
                for distance in range(size + 2):
                    self.check(list(values), distance)
                arrays += 1
        self.assertEqual(arrays, 3280)

    def test_exact_expiry_large_windows_and_no_mutation(self):
        self.check([1, 2, 3, 1], 3, True)
        self.check([1, 2, 3, 1], 2, False)
        self.check([1, 1], 0, False)
        self.check([-10**9, 10**9, -10**9], 2, True)
        self.check(list(range(100000)), 100000, False)
        self.check(list(range(99999)) + [0], 99999, True)
        self.check(list(range(99999)) + [0], 99998, False)
        self.check([7] * 100000, 1, True)


if __name__ == '__main__':
    unittest.main()
