from functools import lru_cache
from itertools import product
import unittest

from python.p0881_boats_to_save_people import Solution


def all_single_or_pair_partitions(weights, limit):
    @lru_cache(None)
    def partition(mask):
        if mask == 0:
            return 0
        first = (mask & -mask).bit_length() - 1
        remaining = mask ^ (1 << first)
        best = 1 + partition(remaining)
        for second in range(len(weights)):
            if remaining >> second & 1 and weights[first] + weights[second] <= limit:
                best = min(best, 1 + partition(remaining ^ (1 << second)))
        return best
    return partition((1 << len(weights)) - 1)


class BoatPartitionTests(unittest.TestCase):
    def check(self, weights, limit, expected=None):
        before = weights[:]
        if expected is None:
            expected = all_single_or_pair_partitions(weights, limit)
        result = Solution().numRescueBoats(weights, limit)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(weights, before)

    def test_every_small_legal_weight_array_against_all_pairings(self):
        checks = 0
        for limit in range(1, 5):
            for size in range(1, 7):
                for weights in product(range(1, limit + 1), repeat=size):
                    self.check(list(weights), limit)
                    checks += 1
        self.assertEqual(checks, 6684)

    def test_maximum_people_weight_and_exact_pair_capacity(self):
        self.check([15000] * 50000, 30000, 25000)
        self.check([30000] * 50000, 30000, 50000)
        self.check([1] * 50000, 1, 50000)
        self.check([1, 29999] * 25000, 30000, 25000)
        self.check([3, 2, 2, 1], 3, 3)


if __name__ == '__main__':
    unittest.main()
