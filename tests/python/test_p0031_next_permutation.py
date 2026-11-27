from itertools import combinations_with_replacement, permutations
import unittest

from python.p0031_next_permutation import Solution


class NextPermutationEnumerationTests(unittest.TestCase):
    def check(self, values, expected):
        result = Solution().nextPermutation(values)
        self.assertIsNone(result)
        self.assertEqual(values, list(expected))

    def test_every_small_multiset_permutation_and_wraparound(self):
        checked = 0
        for size in range(1, 8):
            for values in combinations_with_replacement((0, 1, 2), size):
                ordered = sorted(set(permutations(values)))
                for index, arrangement in enumerate(ordered):
                    self.check(list(arrangement), ordered[(index + 1) % len(ordered)])
                    checked += 1
        self.assertEqual(checked, 3279)

    def test_maximum_length_repeated_successors_and_single_item(self):
        self.check(list(range(100)), list(range(98)) + [99, 98])
        self.check(list(range(99, -1, -1)), list(range(100)))
        self.check([100] * 100, [100] * 100)
        self.check([1, 3, 2, 2], [2, 1, 2, 3])
        self.check([0], [0])
        self.check([1, 1, 5], [1, 5, 1])


if __name__ == '__main__':
    unittest.main()
