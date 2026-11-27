import random
import unittest

from python.p0754_reach_a_number import Solution


class ReachNumberTests(unittest.TestCase):
    def test_all_small_signed_targets_against_actual_layered_left_right_positions(self):
        frontier, first = {0}, {0: 0}
        for step in range(1, 26):
            frontier = {next_position for position in frontier for next_position in (position - step, position + step)}
            for position in frontier:
                first.setdefault(position, step)
        checked = 0
        for target in range(-200, 201):
            if target:
                result = Solution().reachNumber(target)
                self.assertIs(type(result), int)
                self.assertEqual(result, first[target])
                checked += 1
        self.assertEqual(checked, 400)

    def check_minimum_certificate(self, target, expected=None):
        result = Solution().reachNumber(target)
        self.assertIs(type(result), int)
        distance = abs(target)
        total = result * (result + 1) // 2
        self.assertTrue(total >= distance and (total - distance) % 2 == 0)
        self.assertTrue(all(step * (step + 1) // 2 < distance or (step * (step + 1) // 2 - distance) % 2
                            for step in range(result)))
        if expected is not None:
            self.assertEqual(result, expected)

    def test_full_domain_seeded_certificates_triangular_edges_and_extreme_signs(self):
        rng = random.Random(754)
        for _ in range(100):
            self.check_minimum_certificate(rng.choice((-1, 1)) * rng.randrange(1, 10**9 + 1))
        for steps in range(1, 30):
            total = steps * (steps + 1) // 2
            for target in (total - 1, total, total + 1):
                if target:
                    self.check_minimum_certificate(target)
        for target, expected in ((1,1),(2,3),(3,2),(-2,3),(10**9,44723),(-10**9,44723)):
            self.check_minimum_certificate(target, expected)


if __name__ == '__main__':
    unittest.main()
