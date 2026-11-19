from itertools import combinations_with_replacement
import unittest

from python.p0167_two_sum_ii import Solution


class TwoSumSortedTests(unittest.TestCase):
    def test_unique_solutions_match_all_index_pair_oracle(self):
        for length in range(2, 7):
            for values in combinations_with_replacement(range(-2, 3), length):
                for target in range(-4, 5):
                    pairs = [
                        [first + 1, second + 1]
                        for first in range(length)
                        for second in range(first + 1, length)
                        if values[first] + values[second] == target
                    ]
                    if len(pairs) != 1:
                        continue
                    with self.subTest(values=values, target=target):
                        nums = list(values)
                        self.assertEqual(Solution().twoSum(nums, target), pairs[0])
                        self.assertEqual(nums, list(values))

    def test_no_solution_extension_raises_instead_of_reusing_one_index(self):
        for values, target in (([], 0), ([2], 4), ([1, 2], 9), ([0, 0], 1)):
            with self.subTest(values=values, target=target):
                with self.assertRaises(ValueError):
                    Solution().twoSum(values, target)


if __name__ == "__main__":
    unittest.main()
