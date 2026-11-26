import unittest

from python.p0228_summary_ranges import Solution


class SummaryRangesContractTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        result = Solution().summaryRanges(values)
        self.assertIs(type(result), list)
        if expected is not None:
            self.assertEqual(result, expected)
        reconstructed = []
        previous_end = None
        for text in result:
            self.assertIs(type(text), str)
            parts = text.split('->')
            self.assertIn(len(parts), (1, 2))
            endpoints = list(map(int, parts))
            self.assertEqual(parts, [str(value) for value in endpoints])
            start, end = endpoints[0], endpoints[-1]
            if len(parts) == 2:
                self.assertLess(start, end)
            if previous_end is not None:
                self.assertGreater(start, previous_end + 1)
            self.assertLessEqual(end - start + 1, len(before))
            reconstructed.extend(range(start, end + 1))
            previous_end = end
        self.assertEqual(reconstructed, before)
        self.assertEqual(values, before)

    def test_every_subset_against_exact_coverage_and_maximality_contract(self):
        universe = list(range(-5, 6))
        for mask in range(1 << len(universe)):
            self.check([value for bit, value in enumerate(universe) if mask & (1 << bit)])

    def test_negative_ranges_int32_endpoints_and_maximum_input_length(self):
        self.check([], [])
        self.check([0, 1, 2, 4, 5, 7], ['0->2', '4->5', '7'])
        self.check([-3, -2, -1, 1], ['-3->-1', '1'])
        self.check([-2**31, -2**31 + 1, 2**31 - 2, 2**31 - 1], ['-2147483648->-2147483647', '2147483646->2147483647'])
        self.check(list(range(20)), ['0->19'])
        self.check([2**31 - 1], ['2147483647'])


if __name__ == '__main__':
    unittest.main()
