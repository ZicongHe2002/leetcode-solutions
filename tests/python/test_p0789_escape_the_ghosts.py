import unittest
from itertools import combinations_with_replacement, product

from python.p0789_escape_the_ghosts import Solution


def real_moves(positions):
    return {(x + dx,y + dy) for x,y in positions for dx,dy in ((0,0),(1,0),(-1,0),(0,1),(0,-1))}


def literal_simultaneous_safe_paths(ghosts, target):
    unsafe = {tuple(point) for point in ghosts}
    safe = {(0,0)} - unsafe
    goal = tuple(target)
    while safe:
        if goal in safe:
            return True
        if goal in unsafe:
            return False
        unsafe = real_moves(unsafe)
        safe = real_moves(safe) - unsafe
    return False


class EscapeGhostsTests(unittest.TestCase):
    def check(self, ghosts, target, expected=None):
        before = ([point[:] for point in ghosts],target[:])
        result = Solution().escapeGhosts(ghosts,target)
        self.assertIs(type(result),bool)
        self.assertEqual(result,literal_simultaneous_safe_paths(ghosts,target) if expected is None else expected,
                         (ghosts,target))
        self.assertEqual((ghosts,target),before)

    def test_all_small_one_two_ghost_configurations_against_literal_synchronous_moves(self):
        points = list(product(range(-2,3),repeat=2))
        configurations = [(point,) for point in points] + list(combinations_with_replacement(points,2))
        checked = 0
        for ghosts in configurations:
            for target in points:
                self.check([list(point) for point in ghosts],list(target))
                checked += 1
        self.assertEqual(checked,8750)

    def test_official_examples_ties_origin_duplicates_and_coordinate_bounds(self):
        self.check([[1,0],[0,3]],[0,1],True)
        self.check([[1,0]],[2,0],False)
        self.check([[2,0]],[1,0],False)
        self.check([[1,1]],[0,0],True)
        self.check([[0,0]],[0,0],False)
        self.check([[10000,10000]] * 100,[-10000,-10000],True)
        self.check([[10000,10000]] * 99 + [[-10000,10000]],[-10000,-10000],False)
        self.check([[-10000,-10000]] * 100,[10000,10000],True)


if __name__ == '__main__':
    unittest.main()
