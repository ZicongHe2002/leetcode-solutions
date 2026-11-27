import random
import unittest
from functools import lru_cache
from itertools import combinations_with_replacement

from python.p0659_split_array_into_consecutive_subsequences import Solution


def all_assignments(values):
    @lru_cache(None)
    def visit(index, sequences):
        if index == len(values):
            return all(length >= 3 for _, length in sequences)
        value = values[index]
        tried = set()
        for position, (end, length) in enumerate(sequences):
            if end == value - 1 and (end, length) not in tried:
                tried.add((end, length))
                following = list(sequences)
                following[position] = value, min(3, length + 1)
                if visit(index + 1, tuple(sorted(following))):
                    return True
        return visit(index + 1, tuple(sorted(sequences + ((value, 1),))))
    return visit(0, ())


class ConsecutiveSubsequenceTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = all_assignments(values)
        actual = Solution().isPossible(values)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, expected, values if len(values) < 20 else None)
        self.assertEqual(values, before)

    def test_every_small_sorted_multiset_and_samples_against_all_assignments(self):
        checked = 0
        for length in range(1, 11):
            for values in combinations_with_replacement(range(-2, 3), length):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 3002)
        rng = random.Random(659)
        for _ in range(200):
            self.check(sorted(rng.randint(-5, 5) for _ in range(rng.randint(1, 14))))

    def test_maximum_lengths_multiplicity_and_value_bounds(self):
        self.check([0] * 10000, False)
        self.check([0] * 3333 + [1] * 3333 + [2] * 3333 + [3], True)
        self.check([0] * 3333 + [1] * 3333 + [2] * 3334, False)
        self.check(list(range(-1000, 1001)), True)
        self.check([-1000, -999, -998], True)
        self.check([998, 999, 1000], True)
        self.check([999, 1000], False)
        self.check([1, 2, 3, 3, 4, 5], True)
        self.check([1, 2, 3, 4, 4, 5], False)


if __name__ == '__main__':
    unittest.main()
