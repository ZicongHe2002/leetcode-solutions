from functools import lru_cache
from itertools import product
import unittest

from python.p0554_brick_wall import Solution


@lru_cache(None)
def compositions(width):
    if width == 0:
        return ((),)
    return tuple((first,) + remainder for first in range(1, width + 1)
                 for remainder in compositions(width - first))


def interior_geometric_lines_oracle(wall):
    width = sum(wall[0])
    answer = len(wall)
    for doubled_x in range(1, 2 * width):
        crossed = 0
        for row in wall:
            start = 0
            for brick in row:
                end = start + brick
                if 2 * start < doubled_x < 2 * end:
                    crossed += 1
                    break
                start = end
        answer = min(answer, crossed)
    return answer


class InternalBrickEdgeTests(unittest.TestCase):
    def check(self, wall, expected=None):
        before = [row[:] for row in wall]
        identities = tuple(map(id, wall))
        actual = Solution().leastBricks(wall)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, interior_geometric_lines_oracle(wall) if expected is None else expected)
        self.assertEqual(wall, before)
        self.assertEqual(tuple(map(id, wall)), identities)

    def test_all_small_equal_width_walls_against_geometric_line_positions(self):
        walls = 0
        for width in range(1, 7):
            patterns = compositions(width)
            for height in range(1, 4):
                for rows in product(patterns, repeat=height):
                    self.check([list(row) for row in rows])
                    walls += 1
        self.assertEqual(walls, 38877)

    def test_maximum_rows_bricks_single_block_rows_and_large_total_width(self):
        maximum = 2**31 - 1
        self.check([[1, maximum - 1] for _ in range(10000)], 0)
        self.check([[maximum] for _ in range(10000)], 10000)
        self.check([[1] * 10000], 0)
        wide = [[maximum, maximum] for _ in range(4000)]
        wide += [[1, maximum, maximum - 1] for _ in range(4000)]
        self.assertEqual((len(wide), sum(map(len, wide))), (8000, 20000))
        self.assertTrue(all(sum(row) == 2 * maximum for row in wide))
        self.check(wide, 4000)
        self.check([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]], 2)
        self.check([[1], [1], [1]], 3)
        self.check([[1, 2], [2, 1]], 1)


if __name__ == '__main__':
    unittest.main()
