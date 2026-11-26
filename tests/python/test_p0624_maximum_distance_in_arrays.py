from itertools import combinations, combinations_with_replacement, product
import unittest

from python.p0624_maximum_distance_in_arrays import Solution


def all_distinct_array_pairs(arrays):
    return max(abs(a - b) for first, second in combinations(range(len(arrays)), 2)
               for a in arrays[first] for b in arrays[second])


class CrossArrayDistanceTests(unittest.TestCase):
    def check(self, arrays, expected):
        before = [row[:] for row in arrays]
        result = Solution().maxDistance(arrays)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(arrays, before)

    def test_all_small_sorted_row_sequences_against_all_element_pairs(self):
        rows = [row for size in (1, 2) for row in combinations_with_replacement((-2, 0, 3), size)]
        self.assertEqual(len(rows), 9)
        cases = 0
        for count in (2, 3, 4):
            for sequence in product(rows, repeat=count):
                arrays = list(map(list, sequence))
                self.check(arrays, all_distinct_array_pairs(arrays))
                cases += 1
        self.assertEqual(cases, 7371)

    def test_maximum_array_count_row_length_extrema_identity_and_examples(self):
        self.check([[-10000 if index % 2 == 0 else 10000] for index in range(100000)], 20000)
        self.check([list(range(-10000, -9500)) if index % 2 == 0 else list(range(9501, 10001))
                    for index in range(200)], 20000)
        self.check([[0], [-10000, 10000]], 10000)
        self.check([[-10000, 10000], [0]], 10000)
        self.check([[1], [1]], 0)
        self.check([[1, 2, 3], [4, 5], [1, 2, 3]], 4)


if __name__ == '__main__':
    unittest.main()
