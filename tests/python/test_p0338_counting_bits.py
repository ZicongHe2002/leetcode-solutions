import unittest

from python.p0338_counting_bits import Solution


class CountingBitsTests(unittest.TestCase):
    def check(self, n):
        expected = [format(value, 'b').count('1') for value in range(n + 1)]
        result = Solution().countBits(n)
        self.assertEqual(result, expected)
        self.assertTrue(all(type(value) is int for value in result))

    def test_every_small_complete_prefix_against_binary_text(self):
        checks = entries = 0
        for n in range(1025):
            self.check(n)
            checks += 1
            entries += n + 1
        self.assertEqual((checks, entries), (1025, 525825))

    def test_maximum_and_power_of_two_boundaries(self):
        for n in [31, 32, 63, 64, 65535, 65536, 100000]:
            self.check(n)


if __name__ == '__main__':
    unittest.main()
