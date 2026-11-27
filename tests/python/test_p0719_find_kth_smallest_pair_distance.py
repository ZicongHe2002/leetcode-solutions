import random
import unittest
from itertools import product

from python.p0719_find_kth_smallest_pair_distance import Solution


def actual_pair_distances(values):
    return sorted(abs(values[i] - values[j]) for i in range(len(values)) for j in range(i + 1, len(values)))


class KthPairDistanceTests(unittest.TestCase):
    def check(self, values, k, expected=None):
        before = values[:]
        result = Solution().smallestDistancePair(values, k)
        self.assertIs(type(result), int)
        self.assertEqual(result, actual_pair_distances(values)[k - 1] if expected is None else expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_and_ranks_against_sorted_actual_index_pairs(self):
        arrays = checked = 0
        for size in range(2, 8):
            for values in product((0, 1, 3), repeat=size):
                distances = actual_pair_distances(values)
                arrays += 1
                for k, expected in enumerate(distances, 1):
                    self.check(list(values), k, expected)
                    checked += 1
        self.assertEqual((arrays, checked), (3276, 59868))
        rng = random.Random(719)
        for _ in range(200):
            size = rng.randrange(2, 21)
            self.check([rng.randrange(1000001) for _ in range(size)], rng.randrange(1, size * (size - 1) // 2 + 1))

    def test_ten_thousand_elements_duplicate_rank_jumps_and_exact_distance_certificates(self):
        n = 10000
        pairs = n * (n - 1) // 2
        for k in (1, pairs // 2, pairs):
            self.check([0] * n, k, 0)
        zero_pairs = 5000 * 4999
        values = [0] * 5000 + [10**6] * 5000
        for k, expected in ((zero_pairs, 0), (zero_pairs + 1, 10**6), (pairs, 10**6)):
            self.check(values, k, expected)
        distance = 1234
        below = (distance - 1) * n - (distance - 1) * distance // 2
        through = distance * n - distance * (distance + 1) // 2
        for k in (below + 1, through):
            self.check(list(range(n)), k, distance)
        self.check(list(range(n)), pairs, n - 1)
        self.check([1, 3, 1], 1, 0)


if __name__ == '__main__':
    unittest.main()
