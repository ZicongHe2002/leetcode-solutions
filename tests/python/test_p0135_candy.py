import unittest
from functools import lru_cache
from itertools import product

from python.p0135_candy import Solution


@lru_cache(None)
def allocations_by_total(size):
    return sorted(product(range(1, size + 1), repeat=size), key=sum)


def minimum_candy_by_allocations(ratings):
    for allocation in allocations_by_total(len(ratings)):
        valid = True
        for index in range(len(ratings) - 1):
            if ratings[index] < ratings[index + 1] and allocation[index] >= allocation[index + 1]:
                valid = False
                break
            if ratings[index] > ratings[index + 1] and allocation[index] <= allocation[index + 1]:
                valid = False
                break
        if valid:
            return sum(allocation)
    raise AssertionError('A feasible allocation needs at most the number of children per child')


class CandyTests(unittest.TestCase):
    def check(self, ratings, expected=None):
        before = ratings[:]
        if expected is None:
            expected = minimum_candy_by_allocations(ratings)
        result = Solution().candy(ratings)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(ratings, before)

    def test_all_small_ratings_against_all_candy_allocations(self):
        checks = 0
        for size in range(1, 6):
            for ratings in product(range(3), repeat=size):
                self.check(list(ratings))
                checks += 1
        self.assertEqual(checks, 363)

    def test_maximum_lengths_monotone_equal_alternating_and_empty_extension(self):
        expected = 50000 * 50001 // 2
        self.check(list(range(50000)), expected)
        self.check(list(range(50000, 0, -1)), expected)
        self.check([50000] * 50000, 50000)
        self.check([0, 50000] * 25000, 75000)
        self.check([1, 2, 2], 4)
        self.check([1, 0, 2], 5)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
