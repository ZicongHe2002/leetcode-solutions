import string
import unittest
from itertools import product

from python.p0771_jewels_and_stones import Solution


class JewelsStonesTests(unittest.TestCase):
    def check(self, jewels, stones, expected=None):
        result = Solution().numJewelsInStones(jewels, stones)
        self.assertIs(type(result), int)
        self.assertEqual(result, sum(stone == jewel for stone in stones for jewel in jewels)
                         if expected is None else expected, (jewels, stones))

    def test_all_small_unique_jewel_subsets_and_stone_strings_against_pairwise_equality(self):
        checked = 0
        for mask in range(1, 8):
            jewels = ''.join(char for index, char in enumerate('AaB') if mask >> index & 1)
            for size in range(1, 7):
                for chars in product('AaB', repeat=size):
                    self.check(jewels, ''.join(chars))
                    checked += 1
        self.assertEqual(checked, 7644)

    def test_official_examples_maximum_lengths_repetitions_and_case_distinction(self):
        self.check('aA', 'aAAbbbb', 3)
        self.check('z', 'ZZ', 0)
        jewels = string.ascii_letters[:50]
        self.check(jewels, jewels[0] * 50, 50)
        self.check(jewels, 'Z' * 50, 0)
        self.check('a', 'A' * 50, 0)
        self.check('A', 'A' * 50, 50)


if __name__ == '__main__':
    unittest.main()
