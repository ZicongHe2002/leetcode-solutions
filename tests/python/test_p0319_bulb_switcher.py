import unittest

from python.p0319_bulb_switcher import Solution


def physical_toggle_oracle(size):
    bulbs = [False] * size
    for turn in range(1, size + 1):
        for index in range(turn - 1, size, turn):
            bulbs[index] = not bulbs[index]
    return sum(bulbs)


class BulbDivisorParityTests(unittest.TestCase):
    def test_every_small_size_against_all_round_toggles(self):
        for size in range(501):
            actual = Solution().bulbSwitch(size)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, physical_toggle_oracle(size))

    def test_square_neighbors_zero_and_maximum_size(self):
        self.assertEqual(Solution().bulbSwitch(0), 0)
        for root in (1, 2, 3, 10, 99, 100, 999, 1000, 31622):
            self.assertEqual(Solution().bulbSwitch(root * root - 1), root - 1)
            self.assertEqual(Solution().bulbSwitch(root * root), root)
            self.assertEqual(Solution().bulbSwitch(root * root + 1), root)
        self.assertEqual(Solution().bulbSwitch(10**9), 31622)


if __name__ == '__main__':
    unittest.main()
