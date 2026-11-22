import unittest
from itertools import permutations

from python.p0052_n_queens_ii import Solution


def count_legal_column_permutations(size):
    result = checked = 0
    for columns in permutations(range(size)):
        checked += 1
        if all(abs(columns[left] - columns[right]) != right - left
               for left in range(size) for right in range(left + 1, size)):
            result += 1
    return result, checked


class QueenBitCountTests(unittest.TestCase):
    def test_all_original_sizes_against_pairwise_permutation_checks(self):
        checked = 0
        for size in range(1, 10):
            expected, candidates = count_legal_column_permutations(size)
            checked += candidates
            result = Solution().totalNQueens(size)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected)
        self.assertEqual(checked, 409113)

    def test_small_counts_and_repeated_calls_have_no_retained_state(self):
        solver = Solution()
        for size, expected in [(1, 1), (2, 0), (3, 0), (4, 2), (8, 92), (1, 1), (8, 92)]:
            self.assertEqual(solver.totalNQueens(size), expected)


if __name__ == '__main__':
    unittest.main()
