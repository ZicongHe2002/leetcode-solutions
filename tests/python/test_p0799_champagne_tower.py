import unittest
from collections import deque
from fractions import Fraction
from functools import cache

from python.p0799_champagne_tower import Solution


def actual_unit_pour_events(poured, last_row):
    held = [[Fraction(0) for _ in range(row + 1)] for row in range(last_row + 1)]
    for _ in range(poured):
        events = deque([(0,0,Fraction(1))])
        while events:
            row,column,amount = events.popleft()
            kept = min(amount,1 - held[row][column])
            held[row][column] += kept
            excess = amount - kept
            if excess and row < last_row:
                events.append((row + 1,column,excess / 2))
                events.append((row + 1,column + 1,excess / 2))
    return held


def exact_parent_arrivals(poured):
    @cache
    def received(row, column):
        if column < 0 or column > row:
            return Fraction(0)
        if row == 0:
            return Fraction(poured)
        return sum((max(Fraction(0),received(row - 1,parent) - 1) / 2
                    for parent in (column - 1,column)),Fraction(0))
    return received


class ChampagneTowerTests(unittest.TestCase):
    def check(self, poured, row, column, expected):
        result = Solution().champagneTower(poured,row,column)
        self.assertIs(type(result),float)
        self.assertTrue(0.0 <= result <= 1.0)
        self.assertAlmostEqual(result,float(expected),delta=1e-10)

    def test_small_pours_against_individual_exact_capacity_overflow_events(self):
        queries = 0
        for poured in range(31):
            held = actual_unit_pour_events(poured,7)
            for row in range(8):
                for column in range(row + 1):
                    self.check(poured,row,column,held[row][column])
                    queries += 1
        self.assertEqual(queries,1116)

    def test_examples_all_bottom_glasses_and_maximum_pour_against_exact_parent_fractions(self):
        self.check(1,1,1,0)
        self.check(2,1,1,Fraction(1,2))
        self.check(100000009,33,17,1)
        for poured in (0,1,2,3,4,100000009,10**9):
            received = exact_parent_arrivals(poured)
            for column in range(100):
                self.check(poured,99,column,min(Fraction(1),received(99,column)))


if __name__ == '__main__':
    unittest.main()
