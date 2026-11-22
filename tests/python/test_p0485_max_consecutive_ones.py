import unittest
from itertools import product

from python.p0485_max_consecutive_ones import Solution


class ConsecutiveOneTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        expected = max(map(len, ''.join(map(str, values)).split('0')))
        result = Solution().findMaxConsecutiveOnes(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_binary_arrays_and_empty_extension_against_text_segments(self):
        checks = 0
        for size in range(13):
            for values in product((0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 8191)

    def test_maximum_lengths_all_values_alternating_and_terminal_run(self):
        self.check([1] * 100000)
        self.check([0] * 100000)
        self.check([0, 1] * 50000)
        self.check([1, 0, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
