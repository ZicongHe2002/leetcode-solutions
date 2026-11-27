import random
import unittest
from itertools import product

from python.p0698_partition_to_k_equal_sum_subsets import Solution


def actual_set_partitions(values, k):
    groups = []

    def assign(index):
        if index == len(values):
            return len(groups) == k and len({sum(group) for group in groups}) == 1
        for group in groups:
            group.append(values[index])
            possible = assign(index + 1)
            group.pop()
            if possible:
                return True
        if len(groups) < k:
            groups.append([values[index]])
            possible = assign(index + 1)
            groups.pop()
            if possible:
                return True
        return False

    return assign(0)


class PartitionKSubsetsTests(unittest.TestCase):
    def check(self, values, k, expected=None):
        self.assertTrue(all(values.count(value) <= 4 for value in set(values)))
        before = values[:]
        result = Solution().canPartitionKSubsets(values, k)
        self.assertIs(type(result), bool)
        self.assertEqual(result, actual_set_partitions(values, k) if expected is None else expected,
                         (values, k))
        self.assertEqual(values, before)

    def test_all_short_legal_arrays_and_k_against_actual_nonempty_set_partitions(self):
        arrays = checked = 0
        for size in range(1, 7):
            for values in product((1, 2, 3), repeat=size):
                if any(values.count(value) > 4 for value in set(values)):
                    continue
                arrays += 1
                for k in range(1, size + 1):
                    self.check(list(values), k)
                    checked += 1
        self.assertEqual((arrays, checked), (1050, 5766))
        rng = random.Random(698)
        for _ in range(100):
            while True:
                values = [rng.randrange(1, 11) for _ in range(rng.randrange(1, 9))]
                if all(values.count(value) <= 4 for value in set(values)):
                    break
            self.check(values, rng.randrange(1, len(values) + 1))

    def test_sixteen_elements_maximum_values_and_divisible_impossible_targets(self):
        values = [value for value in (1, 2, 3, 4) for _ in range(4)]
        self.check(values, 4, True)
        self.check(values, 1, True)
        self.check(values, 16, False)
        self.check([value for value in (9997, 9998, 9999, 10000) for _ in range(4)], 4, True)
        self.check([value for value in (2, 4, 6, 10) for _ in range(4)], 8, False)
        self.check([4, 3, 2, 3, 5, 2, 1], 4, True)
        self.check([1, 2, 3, 4], 3, False)
        self.check([1, 1, 1, 1], 4, True)


if __name__ == '__main__':
    unittest.main()
