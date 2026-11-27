from itertools import combinations, product
import unittest

from python.p0575_distribute_candies import Solution


def all_half_selections(values):
    best = 0
    for selected in combinations(range(len(values)), len(values) // 2):
        distinct = []
        for index in selected:
            if values[index] not in distinct:
                distinct.append(values[index])
        best = max(best, len(distinct))
    return best


class CandyTypeTests(unittest.TestCase):
    def check(self, values, expected):
        before = values[:]
        result = Solution().distributeCandies(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_even_arrays_against_exact_half_subsets(self):
        checks = 0
        for size in (2, 4, 6, 8):
            for values in product((-1, 0, 2), repeat=size):
                self.check(list(values), all_half_selections(values))
                checks += 1
        self.assertEqual(checks, 7380)

    def test_ten_thousand_candies_and_signed_type_boundaries(self):
        self.check([4] * 10000, 1)
        self.check(list(range(10000)), 5000)
        self.check(list(range(5000)) * 2, 5000)
        self.check([-100000, 100000], 1)
        self.check([-100000, -100000, 100000, 100000], 2)
        self.check([1, 1, 2, 2, 3, 3], 3)


if __name__ == '__main__':
    unittest.main()
