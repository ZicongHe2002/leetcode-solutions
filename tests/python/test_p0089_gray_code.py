import unittest

from python.p0089_gray_code import Solution


class GrayCodeCyclePropertyTests(unittest.TestCase):
    def test_all_supported_widths_value_coverage_and_each_cycle_edge(self):
        checked_values = 0
        for bits in range(1, 17):
            result = Solution().grayCode(bits)
            self.assertIs(type(result), list)
            self.assertEqual(len(result), 1 << bits)
            self.assertEqual(result[0], 0)
            self.assertTrue(all(type(value) is int for value in result))
            self.assertEqual(set(result), set(range(1 << bits)))
            for index, value in enumerate(result):
                following = result[(index + 1) % len(result)]
                self.assertEqual((value ^ following).bit_count(), 1)
                self.assertEqual(value, index ^ (index >> 1))
            checked_values += len(result)
        self.assertEqual(checked_values, 131070)

    def test_boundary_examples_and_fresh_results_between_calls(self):
        solution = Solution()
        self.assertEqual(solution.grayCode(1), [0, 1])
        self.assertEqual(solution.grayCode(2), [0, 1, 3, 2])
        previous = solution.grayCode(3)
        previous[0] = 100
        previous.append(100)
        self.assertEqual(solution.grayCode(3), [0, 1, 3, 2, 6, 7, 5, 4])
        self.assertEqual(solution.grayCode(1), [0, 1])


if __name__ == '__main__':
    unittest.main()
