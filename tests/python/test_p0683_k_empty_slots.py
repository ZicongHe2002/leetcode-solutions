import unittest
from itertools import permutations

from python.p0683_k_empty_slots import Solution


def daily_simulation(bulbs, k):
    on = [False] * len(bulbs)
    for day, position in enumerate(bulbs, 1):
        on[position - 1] = True
        for left in range(len(bulbs) - k - 1):
            right = left + k + 1
            if on[left] and on[right] and not any(on[left + 1:right]):
                return day
    return -1


class KEmptySlotsTests(unittest.TestCase):
    def check(self, bulbs, k, expected=None):
        before = bulbs[:]
        result = Solution().kEmptySlots(bulbs, k)
        self.assertIs(type(result), int)
        self.assertEqual(result, daily_simulation(bulbs, k) if expected is None else expected,
                         (bulbs[:20], k))
        self.assertEqual(bulbs, before)

    def test_all_small_permutations_and_gaps_against_actual_daily_lights(self):
        arrangements = checked = 0
        for n in range(1, 8):
            for order in permutations(range(1, n + 1)):
                arrangements += 1
                for k in range(n + 1):
                    self.check(list(order), k)
                    checked += 1
        self.assertEqual((arrangements, checked), (5913, 46232))

    def test_twenty_thousand_bulbs_empty_interior_and_impossible_large_gaps(self):
        increasing = list(range(1, 20001))
        self.check(increasing, 0, 2)
        self.check(increasing, 1, -1)
        self.check(increasing, 19998, -1)
        self.check(increasing, 20000, -1)
        self.check(increasing[::-1], 0, 2)
        self.check([1, 20000] + list(range(2, 20000)), 19998, 2)
        self.check(list(range(1, 20001, 2)) + list(range(2, 20001, 2)), 1, 2)
        self.check([1, 3, 2], 1, 2)
        self.check([1], 0, -1)


if __name__ == '__main__':
    unittest.main()
