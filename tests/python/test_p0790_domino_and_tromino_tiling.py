import unittest
from functools import cache

from python.p0790_domino_and_tromino_tiling import Solution


def exact_full_cell_covers(width):
    shapes = (((0,0),(1,0)),((0,0),(0,1)),
              ((0,0),(1,0),(0,1)),((0,0),(1,0),(1,1)),
              ((0,0),(0,1),(1,1)),((1,0),(0,1),(1,1)))
    placements = set()
    for row in range(2):
        for column in range(width):
            for shape in shapes:
                cells = [(row + dr,column + dc) for dr,dc in shape]
                if all(0 <= r < 2 and 0 <= c < width for r,c in cells):
                    placements.add(sum(1 << (r * width + c) for r,c in cells))
    cover = [[tile for tile in placements if tile >> cell & 1] for cell in range(2 * width)]
    full = (1 << (2 * width)) - 1

    @cache
    def count(occupied):
        if occupied == full:
            return 1
        cell = next(cell for cell in range(2 * width) if not (occupied >> cell & 1))
        return sum(count(occupied | tile) for tile in cover[cell] if not occupied & tile)

    return count(0)


def exact_column_profile_counts(limit):
    # Column-major bits: current top/bottom, then next top/bottom.
    tiles = (0b0011,0b0101,0b1010,0b0111,0b1011,0b1101,0b1110)
    transitions = [[0] * 4 for _ in range(4)]
    for incoming in range(4):
        def fill(mask):
            if mask & 3 == 3:
                transitions[incoming][mask >> 2] += 1
                return
            first = 1 if not mask & 1 else 2
            for tile in tiles:
                if tile & first and not tile & mask:
                    fill(mask | tile)
        fill(incoming)
    vector, result = [1,0,0,0], [1]
    for _ in range(limit):
        following = [sum(vector[source] * transitions[source][target] for source in range(4)) for target in range(4)]
        vector = following
        result.append(vector[0])
    return result


class DominoTrominoTests(unittest.TestCase):
    def check(self, n, expected):
        result = Solution().numTilings(n)
        self.assertIs(type(result),int)
        self.assertEqual(result,expected,n)
        self.assertTrue(0 <= result < 10**9 + 7)

    def test_every_small_width_against_literal_rotated_tile_exact_covers(self):
        for width in range(1,11):
            self.check(width,exact_full_cell_covers(width))

    def test_every_remaining_legal_width_against_exact_column_mask_transfer_counts(self):
        expected = exact_column_profile_counts(1000)
        self.assertEqual(expected[:4],[1,1,2,5])
        for width in range(11,1001):
            self.check(width,expected[width] % (10**9 + 7))


if __name__ == '__main__':
    unittest.main()
