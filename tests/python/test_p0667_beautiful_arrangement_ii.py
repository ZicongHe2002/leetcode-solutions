import unittest

from python.p0667_beautiful_arrangement_ii import Solution


class ArrangementConstructionTests(unittest.TestCase):
    def check(self, n, k):
        result = Solution().constructArray(n, k)
        self.assertIs(type(result), list)
        self.assertEqual(len(result), n)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(set(result), set(range(1, n + 1)))
        gaps = {abs(first - second) for first, second in zip(result, result[1:])}
        self.assertEqual(len(gaps), k, (n, k))

    def test_every_small_valid_parameter_pair_against_output_contract(self):
        checked = 0
        for n in range(2, 101):
            for k in range(1, n):
                self.check(n, k)
                checked += 1
        self.assertEqual(checked, 4950)

    def test_maximum_size_extreme_and_middle_gap_counts(self):
        for k in (1, 2, 5000, 9999):
            self.check(10000, k)


if __name__ == '__main__':
    unittest.main()
