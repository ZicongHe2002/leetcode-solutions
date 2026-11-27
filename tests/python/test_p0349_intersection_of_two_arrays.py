from itertools import product
import unittest

from python.p0349_intersection_of_two_arrays import Solution


def direct_members(first, second):
    candidates = sorted(first + second)
    return [value for index, value in enumerate(candidates)
            if (index == 0 or value != candidates[index - 1])
            and first.count(value) > 0 and second.count(value) > 0]


class UniqueArrayIntersectionTests(unittest.TestCase):
    def check(self, first, second):
        before = (first[:], second[:])
        result = Solution().intersection(first, second)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(sorted(result), direct_members(first, second))
        self.assertEqual((first, second), before)

    def test_all_small_array_pairs_against_direct_counts(self):
        arrays = [list(values) for size in range(1, 5) for values in product((0, 1, 2), repeat=size)]
        checks = 0
        for first in arrays:
            for second in arrays:
                self.check(first, second)
                checks += 1
        self.assertEqual((len(arrays), checks), (120, 14400))

    def test_maximum_lengths_duplicates_disjoint_and_value_limits(self):
        self.check(list(range(1000)), list(range(1, 1001)))
        self.check([1000] * 1000, [1000] * 1000)
        self.check([0] * 1000, [1000] * 1000)
        self.check([0, 1000], [1000, 0, 1000])


if __name__ == '__main__':
    unittest.main()
