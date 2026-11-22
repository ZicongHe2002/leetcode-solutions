from itertools import combinations, product
import unittest

from python.p0016_3sum_closest import Solution


class ClosestThreeSumCombinationTests(unittest.TestCase):
    def check(self, values, target, expected):
        before = values[:]
        result = Solution().threeSumClosest(values, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_with_unique_nearest_sum(self):
        arrays = checks = skipped_ties = 0
        for size in range(3, 7):
            for values in product((-2, -1, 0, 1, 2), repeat=size):
                arrays += 1
                sums = {sum(triple) for triple in combinations(values, 3)}
                for target in (-7, -3, 0, 3, 7):
                    distance = min(abs(total - target) for total in sums)
                    nearest = [total for total in sums if abs(total - target) == distance]
                    if len(nearest) == 1:
                        self.check(list(values), target, nearest[0])
                        checks += 1
                    else:
                        skipped_ties += 1
        self.assertEqual((arrays, checks, skipped_ties), (19500, 94120, 3380))

    def test_maximum_length_value_limits_and_target_outside_sum_range(self):
        values = [-1000] * 250 + [1000] * 250
        for target, expected in ((10000, 3000), (-10000, -3000), (999, 1000), (-999, -1000)):
            self.check(values, target, expected)
        self.check([-1, 2, 1, -4], 1, 2)
        self.check([0, 0, 0], 1, 0)
        self.check([1, 2, 3], 6, 6)


if __name__ == '__main__':
    unittest.main()
