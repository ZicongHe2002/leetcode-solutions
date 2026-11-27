from itertools import permutations
from math import factorial
import unittest

from python.p0060_permutation_sequence import Solution


def rank_by_smaller_suffix_counts(value):
    return 1 + sum(sum(other < character for other in value[index + 1:])
                   * factorial(len(value) - index - 1) for index, character in enumerate(value))


class PermutationSequenceEnumerationTests(unittest.TestCase):
    def check(self, n, k, expected=None):
        result = Solution().getPermutation(n, k)
        self.assertIs(type(result), str)
        self.assertEqual(sorted(result), [str(value) for value in range(1, n + 1)])
        self.assertEqual(rank_by_smaller_suffix_counts(result), k)
        if expected is not None:
            self.assertEqual(result, expected)

    def test_every_rank_in_all_small_permutation_sequences(self):
        checked = 0
        for n in range(1, 8):
            for k, candidate in enumerate(permutations(''.join(str(value) for value in range(1, n + 1))), 1):
                self.check(n, k, ''.join(candidate))
                checked += 1
        self.assertEqual(checked, 5913)

    def test_largest_n_first_last_middle_ranks_and_fixed_examples(self):
        self.check(9, 1, '123456789')
        self.check(9, factorial(9), '987654321')
        for k in (2, 100, 10000, factorial(9) // 2, factorial(9) // 2 + 1, factorial(9) - 1):
            self.check(9, k)
        self.check(3, 3, '213')
        self.check(4, 9, '2314')


if __name__ == '__main__':
    unittest.main()
