from itertools import product
import unittest

from python.p0198_house_robber import Solution


class HouseRobberTests(unittest.TestCase):
    def test_small_inputs_match_all_legal_subsets(self):
        cases = 0
        for length in range(7):
            for values in product(range(4), repeat=length):
                expected = max(
                    sum(values[index] for index in range(length) if mask & (1 << index))
                    for mask in range(1 << length)
                    if not mask & (mask << 1)
                )
                nums = list(values)
                with self.subTest(values=values):
                    self.assertEqual(Solution().rob(nums), expected)
                    self.assertEqual(nums, list(values))
                cases += 1
        self.assertEqual(cases, 5461)

    def test_boundaries_and_mixed_parity_choice(self):
        for nums, expected in (([7], 7), ([0] * 100, 0), ([400] * 100, 20000), ([2, 1, 1, 2], 4)):
            with self.subTest(nums=nums):
                self.assertEqual(Solution().rob(nums), expected)


if __name__ == "__main__":
    unittest.main()
