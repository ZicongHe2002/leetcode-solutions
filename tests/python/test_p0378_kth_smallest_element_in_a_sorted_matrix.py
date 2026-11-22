import unittest
from itertools import product

from python.p0378_kth_smallest_element_in_a_sorted_matrix import Solution


class SortedMatrixSelectionTests(unittest.TestCase):
    def check(self, matrix, k, expected=None):
        before = [row[:] for row in matrix]
        if expected is None:
            expected = sorted(value for row in matrix for value in row)[k - 1]
        result = Solution().kthSmallest(matrix, k)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(matrix, before)

    def test_all_small_row_column_sorted_matrices_against_flat_sort(self):
        matrices = checks = 0
        for size in range(1, 4):
            for flat in product((-1, 0, 1), repeat=size * size):
                if any(flat[row * size + column] > flat[row * size + column + 1]
                       for row in range(size) for column in range(size - 1)):
                    continue
                if any(flat[row * size + column] > flat[(row + 1) * size + column]
                       for row in range(size - 1) for column in range(size)):
                    continue
                matrix = [list(flat[row * size:(row + 1) * size]) for row in range(size)]
                matrices += 1
                for k in range(1, size * size + 1):
                    self.check(matrix, k)
                    checks += 1
        self.assertEqual((matrices, checks), (198, 1658))

    def test_maximum_dimensions_rank_endpoints_duplicates_and_extreme_values(self):
        matrix = [[row * 300 + column for column in range(300)] for row in range(300)]
        for k in (1, 45000, 90000):
            self.check(matrix, k, k - 1)
        self.check([[-10**9] * 300 for _ in range(300)], 90000, -10**9)
        blocks = [[-10**9] * 150 + [10**9] * 150 for _ in range(300)]
        self.check(blocks, 45000, -10**9)
        self.check(blocks, 45001, 10**9)
        self.check([[10**9]], 1, 10**9)


if __name__ == '__main__':
    unittest.main()
