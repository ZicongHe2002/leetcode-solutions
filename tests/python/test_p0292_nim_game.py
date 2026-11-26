import unittest

from python.p0292_nim_game import Solution


class NimRetrogradeTests(unittest.TestCase):
    def test_every_small_position_against_all_legal_moves(self):
        winning = [False] * 1025
        for stones in range(1, len(winning)):
            winning[stones] = any(not winning[stones - taken] for taken in (1, 2, 3) if taken <= stones)
            actual = Solution().canWinNim(stones)
            self.assertIs(type(actual), bool)
            self.assertEqual(actual, winning[stones])

    def test_direct_finishes_and_int32_upper_boundary(self):
        for stones in (1, 2, 3, 5, 6, 7, 2**31 - 3, 2**31 - 2, 2**31 - 1):
            self.assertTrue(Solution().canWinNim(stones))
        for stones in (4, 8, 12, 2**31 - 4):
            self.assertFalse(Solution().canWinNim(stones))


if __name__ == '__main__':
    unittest.main()
