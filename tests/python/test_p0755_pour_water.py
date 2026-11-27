import unittest
from itertools import product

from python.p0755_pour_water import Solution


def all_paths_to_each_landing(heights, volume, source):
    levels = heights[:]
    for _ in range(volume):
        chosen = source
        for direction in (-1, 1):
            targets = range(source - 1, -1, -1) if direction == -1 else range(source + 1, len(levels))
            valid = [target for target in targets
                     if levels[target] < levels[source]
                     and all(levels[position + direction] <= levels[position]
                             for position in range(source, target, direction))]
            if valid:
                chosen = min(valid, key=lambda target: (levels[target], abs(target - source)))
                break
        levels[chosen] += 1
    return levels


class PourWaterTests(unittest.TestCase):
    def check(self, heights, volume, k, expected=None):
        before = heights[:]
        result = Solution().pourWater(heights, volume, k)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result, all_paths_to_each_landing(heights, volume, k) if expected is None else expected,
                         (heights[:20], volume, k))
        self.assertEqual(len(result), len(heights))
        self.assertEqual(sum(result), sum(heights) + volume)
        self.assertEqual(heights, before)

    def test_all_small_terrain_source_and_volume_combinations_against_full_path_candidates(self):
        arrays = checked = 0
        for size in range(1, 7):
            for heights in product((0, 1, 2), repeat=size):
                arrays += 1
                for k in range(size):
                    for volume in range(6):
                        self.check(list(heights), volume, k)
                        checked += 1
        self.assertEqual((arrays, checked), (1092, 36090))

    def test_official_examples_flat_closed_forms_zero_volume_and_output_above_initial_bound(self):
        self.check([2,1,1,2,1,2,2], 4, 3, [2,2,2,3,2,2,2])
        self.check([1,2,3,4], 2, 2, [2,3,3,4])
        self.check([3,1,3], 5, 1, [4,4,4])
        self.check([99], 2000, 0, [2099])
        self.check([0] * 100, 0, 50, [0] * 100)
        for k in (0, 50, 99):
            self.check([0] * 100, 2000, k, [20] * 100)
        self.check([99] * 100, 2000, 50, [119] * 100)


if __name__ == '__main__':
    unittest.main()
