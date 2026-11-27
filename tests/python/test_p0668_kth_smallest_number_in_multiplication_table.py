import unittest
from bisect import bisect_right

from python.p0668_kth_smallest_number_in_multiplication_table import Solution


def range_search_count(rows, columns, value):
    return sum(bisect_right(range(row, row * (columns + 1), row), value)
               for row in range(1, rows + 1))


class MultiplicationRankTests(unittest.TestCase):
    def check(self, rows, columns, rank, expected):
        actual = Solution().findKthNumber(rows, columns, rank)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected, (rows, columns, rank))

    def test_every_small_table_and_rank_against_sorted_actual_cell_products(self):
        checked = 0
        for rows in range(1, 21):
            for columns in range(1, 21):
                values = sorted(row * column for row in range(1, rows + 1)
                                for column in range(1, columns + 1))
                for rank, expected in enumerate(values, 1):
                    self.check(rows, columns, rank, expected)
                    checked += 1
        self.assertEqual(checked, 44100)

    def test_maximum_dimensions_duplicate_ranks_and_independent_row_search(self):
        self.check(30000, 30000, 1, 1)
        self.check(30000, 30000, 900000000, 900000000)
        self.check(30000, 30000, 899999999, 899970000)
        self.check(1, 30000, 15000, 15000)
        self.check(30000, 1, 29999, 29999)
        for rows, columns, rank in ((30000, 30000, 450000000),
                                    (30000, 29999, 123456789),
                                    (12345, 23456, 111111111)):
            actual = Solution().findKthNumber(rows, columns, rank)
            self.assertIs(type(actual), int)
            self.assertLess(range_search_count(rows, columns, actual - 1), rank)
            self.assertGreaterEqual(range_search_count(rows, columns, actual), rank)


if __name__ == '__main__':
    unittest.main()
