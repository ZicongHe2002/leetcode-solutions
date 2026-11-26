import random
import unittest
from collections import Counter
from itertools import permutations

from python.p0645_set_mismatch import Solution


def explicit_counts(values):
    counts = Counter(values)
    duplicate = next(value for value, count in counts.items() if count == 2)
    missing = next(value for value in range(1, len(values) + 1) if value not in counts)
    return [duplicate, missing]


class SetMismatchTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = explicit_counts(values)
        result = Solution().findErrorNums(values)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_every_small_replacement_and_distinct_permutation_against_counter(self):
        checks = 0
        for size in range(2, 7):
            for duplicate in range(1, size + 1):
                for missing in range(1, size + 1):
                    if duplicate == missing:
                        continue
                    values = list(range(1, size + 1))
                    values[missing - 1] = duplicate
                    for ordering in set(permutations(values)):
                        self.check(list(ordering))
                        checks += 1
        self.assertEqual(checks, 12164)
        rng = random.Random(645)
        for _ in range(100):
            size = rng.randint(2, 100)
            duplicate, missing = rng.sample(range(1, size + 1), 2)
            values = list(range(1, size + 1))
            values[missing - 1] = duplicate
            rng.shuffle(values)
            self.check(values)

    def test_maximum_length_high_bit_and_required_result_order(self):
        values = list(range(1, 10001))
        values[0] = 10000
        self.check(values, [10000, 1])
        values = list(range(1, 10001))
        values[-1] = 1
        self.check(values, [1, 10000])
        self.check([2, 2], [2, 1])
        self.check([1, 1], [1, 2])


if __name__ == '__main__':
    unittest.main()
