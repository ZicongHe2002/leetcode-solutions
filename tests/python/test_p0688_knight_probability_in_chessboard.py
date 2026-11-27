import math
import unittest
from fractions import Fraction
from itertools import product

from python.p0688_knight_probability_in_chessboard import Solution


def knight_moves():
    return [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3) if abs(dr * dc) == 2]


def explicit_sequences(n, k, row, column):
    successes = 0
    for sequence in product(knight_moves(), repeat=k):
        r, c = row, column
        for dr, dc in sequence:
            r, c = r + dr, c + dc
            if not (0 <= r < n and 0 <= c < n):
                break
        else:
            successes += 1
    return float(Fraction(successes, 8**k))


def forward_distribution(n, k, row, column):
    current = {(row, column): 1}
    for _ in range(k):
        following = {}
        for (r, c), count in current.items():
            for dr, dc in knight_moves():
                target = (r + dr, c + dc)
                if 0 <= target[0] < n and 0 <= target[1] < n:
                    following[target] = following.get(target, 0) + count
        current = following
    return float(Fraction(sum(current.values()), 8**k))


class KnightProbabilityTests(unittest.TestCase):
    def check(self, n, k, row, column, expected):
        result = Solution().knightProbability(n, k, row, column)
        self.assertIs(type(result), float)
        self.assertTrue(0.0 <= result <= 1.0)
        self.assertTrue(math.isclose(result, expected, rel_tol=1e-14, abs_tol=1e-15),
                        (n, k, row, column, result, expected))

    def test_all_small_starts_and_move_counts_against_actual_choice_sequences(self):
        checked = 0
        for n in range(1, 6):
            for row in range(n):
                for column in range(n):
                    for k in range(5):
                        self.check(n, k, row, column, explicit_sequences(n, k, row, column))
                        checked += 1
        self.assertEqual(checked, 275)

    def test_maximum_board_moves_forward_distribution_symmetry_and_survival(self):
        for n, k, row, column in ((25, 100, 12, 12), (25, 100, 0, 0), (25, 100, 24, 12),
                                   (1, 100, 0, 0), (2, 1, 1, 1), (3, 2, 0, 0)):
            self.check(n, k, row, column, forward_distribution(n, k, row, column))
        corner = Solution().knightProbability(25, 100, 0, 0)
        for row, column in ((0, 24), (24, 0), (24, 24)):
            self.check(25, 100, row, column, corner)
        probabilities = [Solution().knightProbability(5, k, 2, 2) for k in range(11)]
        self.assertEqual(probabilities[0], 1.0)
        self.assertTrue(all(a >= b for a, b in zip(probabilities, probabilities[1:])))


if __name__ == '__main__':
    unittest.main()
