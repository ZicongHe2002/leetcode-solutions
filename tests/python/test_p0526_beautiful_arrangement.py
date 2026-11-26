from itertools import permutations
import unittest

from python.p0526_beautiful_arrangement import Solution


def all_permutations_oracle(n):
    return sum(all(value % position == 0 or position % value == 0
                   for position, value in enumerate(values, 1))
               for values in permutations(range(1, n + 1)))


def reverse_position_enumeration(n):
    used = [False] * (n + 1)

    def fill(position):
        if position == 0:
            return 1
        total = 0
        for value in range(1, n + 1):
            if not used[value] and (value % position == 0 or position % value == 0):
                used[value] = True
                total += fill(position - 1)
                used[value] = False
        return total

    return fill(n)


class DivisibilityPermutationCountTests(unittest.TestCase):
    def test_small_domain_against_every_permutation(self):
        for n in range(1, 9):
            actual = Solution().countArrangement(n)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, all_permutations_oracle(n))
        self.assertEqual(Solution().countArrangement(1), 1)
        self.assertEqual(Solution().countArrangement(2), 2)

    def test_remaining_original_domain_against_uncached_reverse_position_search(self):
        counts = {}
        for n in range(9, 16):
            actual = Solution().countArrangement(n)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, reverse_position_enumeration(n))
            counts[n] = actual
        self.assertEqual(counts[15], 24679)


if __name__ == '__main__':
    unittest.main()
