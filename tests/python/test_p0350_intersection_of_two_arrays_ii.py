from itertools import product
import unittest

from python.p0350_intersection_of_two_arrays_ii import Solution


def consume_matching_positions(first, second):
    available = second[:]
    result = []
    for value in first:
        if value in available:
            result.append(value)
            available.remove(value)
    return result


class MultisetArrayIntersectionTests(unittest.TestCase):
    def check(self, first, second):
        before = (first[:], second[:])
        result = Solution().intersect(first, second)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(sorted(result), sorted(consume_matching_positions(first, second)))
        self.assertEqual((first, second), before)

    def test_all_small_array_pairs_against_individual_position_consumption(self):
        arrays = [list(values) for size in range(1, 5) for values in product((0, 1, 2), repeat=size)]
        checks = 0
        for first in arrays:
            for second in arrays:
                self.check(first, second)
                checks += 1
        self.assertEqual(checks, 14400)

    def test_maximum_lengths_asymmetric_counts_and_value_limits(self):
        self.check([1000] * 1000, [1000] * 999 + [0])
        self.check(list(range(1000)), list(range(1, 1001)))
        self.check([0], [0] * 1000)
        self.check([0] * 1000, [1000])


if __name__ == '__main__':
    unittest.main()
