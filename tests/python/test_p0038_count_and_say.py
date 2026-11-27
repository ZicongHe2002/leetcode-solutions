from itertools import groupby
import unittest

from python.p0038_count_and_say import Solution


class CountAndSayGroupingOracleTests(unittest.TestCase):
    def test_every_supported_term_against_standard_groupby(self):
        expected = '1'
        for n in range(1, 31):
            result = Solution().countAndSay(n)
            self.assertIs(type(result), str)
            self.assertEqual(result, expected)
            if n < 30:
                expected = ''.join(str(sum(1 for _ in run)) + digit for digit, run in groupby(expected))

    def test_fixed_first_terms_and_maximum_term_inverse_run_description(self):
        for n, expected in enumerate(('1', '11', '21', '1211', '111221', '312211'), 1):
            self.assertEqual(Solution().countAndSay(n), expected)
        term = Solution().countAndSay(30)
        self.assertEqual(len(term), 4462)
        self.assertEqual(len(term) % 2, 0)
        counts = [int(term[index]) for index in range(0, len(term), 2)]
        digits = [term[index] for index in range(1, len(term), 2)]
        self.assertTrue(all(1 <= count <= 3 for count in counts))
        self.assertTrue(all(first != second for first, second in zip(digits, digits[1:])))
        decoded = ''.join(digit * count for digit, count in zip(digits, counts))
        self.assertEqual(decoded, Solution().countAndSay(29))


if __name__ == '__main__':
    unittest.main()
