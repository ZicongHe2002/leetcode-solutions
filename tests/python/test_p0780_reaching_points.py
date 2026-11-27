import random
import unittest
from itertools import product

from python.p0780_reaching_points import Solution


def actual_forward_states(sx, sy, limit):
    seen, frontier = {(sx,sy)}, [(sx,sy)]
    while frontier:
        x,y = frontier.pop()
        for following in ((x + y,y),(x,x + y)):
            if max(following) <= limit and following not in seen:
                seen.add(following)
                frontier.append(following)
    return seen


class ReachingPointsTests(unittest.TestCase):
    def check(self, sx, sy, tx, ty, expected):
        result = Solution().reachingPoints(sx,sy,tx,ty)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected, (sx,sy,tx,ty))

    def test_all_small_starts_and_targets_against_actual_forward_addition_graphs(self):
        checked = 0
        for sx,sy in product(range(1,6), repeat=2):
            reachable = actual_forward_states(sx,sy,30)
            for tx,ty in product(range(1,31), repeat=2):
                self.check(sx,sy,tx,ty,(tx,ty) in reachable)
                checked += 1
        self.assertEqual(checked,22500)

    def test_seeded_literal_forward_paths_official_examples_and_maximum_boundaries(self):
        rng = random.Random(780)
        for _ in range(100):
            sx,sy = rng.randrange(1,11),rng.randrange(1,11)
            x,y = sx,sy
            for _ in range(50):
                choices = [point for point in ((x+y,y),(x,x+y)) if max(point) <= 10**9]
                if not choices:
                    break
                x,y = rng.choice(choices)
            self.check(sx,sy,x,y,True)
        for query in ((1,1,3,5,True),(1,1,2,2,False),(1,1,1,1,True),
                      (1,1,1,10**9,True),(1,2,10**9,2,False),
                      (1,2,10**9-1,2,True),(10**9,10**9,10**9,10**9,True),
                      (10**9,1,1,10**9,False)):
            self.check(*query)


if __name__ == '__main__':
    unittest.main()
