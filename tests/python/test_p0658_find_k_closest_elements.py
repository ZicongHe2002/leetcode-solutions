import unittest
from itertools import combinations_with_replacement

from python.p0658_find_k_closest_elements import Solution


def preference_oracle(arr, count, target):
    return sorted(sorted(arr, key=lambda value: (abs(value - target), value))[:count])


class ClosestElementTests(unittest.TestCase):
    def check(self, arr, count, target):
        before = arr[:]
        result = Solution().findClosestElements(arr, count, target)
        self.assertEqual(result, preference_oracle(arr, count, target))
        self.assertEqual(arr, before)
        self.assertIsNot(result, arr)

    def test_all_small_sorted_arrays_counts_and_targets_against_preference_sort(self):
        arrays = checks = 0
        for size in range(1, 8):
            for values in combinations_with_replacement(range(-2, 3), size):
                arrays += 1
                for count in range(1, size + 1):
                    for target in range(-3, 4):
                        self.check(list(values), count, target)
                        checks += 1
        self.assertEqual((arrays, checks), (791, 32340))

    def test_ties_duplicate_endpoints_and_maximum_contract(self):
        self.check([1, 2, 3, 4, 5], 4, 3)
        self.check([1, 2, 3, 4, 5], 4, -1)
        self.check([1, 1, 1, 10], 1, 9)
        self.check([1, 1, 1, 2, 2, 2], 3, 2)
        self.check([-10000, 10000], 1, 0)
        arr = list(range(-5000, 5000))
        self.check(arr, 10000, 10000)
        self.check(arr, 1, -10000)
        self.check(arr, 10, 10000)


if __name__ == '__main__':
    unittest.main()
