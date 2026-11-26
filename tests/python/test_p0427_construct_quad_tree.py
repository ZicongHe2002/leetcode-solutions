from itertools import product
import unittest

from python.p0427_construct_quad_tree import Solution


def decode_and_check_structure(root, size):
    pixels = [[None] * size for _ in range(size)]
    seen = set()
    def paint(node, row, column, width):
        if id(node) in seen:
            raise AssertionError('quad tree reuses a node')
        seen.add(id(node))
        if type(node.val) is not bool or type(node.isLeaf) is not bool:
            raise AssertionError('node fields must be booleans')
        children = (node.topLeft, node.topRight, node.bottomLeft, node.bottomRight)
        if node.isLeaf:
            if any(child is not None for child in children):
                raise AssertionError('leaf has children')
            for x in range(row, row + width):
                for y in range(column, column + width):
                    pixels[x][y] = int(node.val)
            return
        if width == 1 or any(child is None for child in children):
            raise AssertionError('invalid internal quadrant')
        if all(child.isLeaf for child in children) and len({child.val for child in children}) == 1:
            raise AssertionError('uniform quadrant was not compressed')
        half = width // 2
        for child, dx, dy in zip(children, (0, 0, half, half), (0, half, 0, half)):
            paint(child, row + dx, column + dy, half)
    paint(root, 0, 0, size)
    return pixels, len(seen)


class QuadTreePixelReconstructionTests(unittest.TestCase):
    def check(self, grid, expected_nodes=None):
        before = [row[:] for row in grid]
        row_ids = [id(row) for row in grid]
        root = Solution().construct(grid)
        pixels, count = decode_and_check_structure(root, len(grid))
        self.assertEqual(pixels, grid)
        self.assertEqual(grid, before)
        self.assertEqual([id(row) for row in grid], row_ids)
        if expected_nodes is not None:
            self.assertEqual(count, expected_nodes)

    def test_every_binary_grid_at_sizes_one_two_and_four(self):
        grids = 0
        for size in (1, 2, 4):
            for cells in product((0, 1), repeat=size * size):
                self.check([list(cells[row * size:(row + 1) * size]) for row in range(size)])
                grids += 1
        self.assertEqual(grids, 65554)

    def test_maximum_grid_uniform_compression_and_quadrant_order(self):
        self.check([[0] * 64 for _ in range(64)], 1)
        self.check([[1] * 64 for _ in range(64)], 1)
        self.check([[(row + column) % 2 for column in range(64)] for row in range(64)], 5461)
        self.check([[0] * 32 + [1] * 32 for _ in range(64)], 5)


if __name__ == '__main__':
    unittest.main()
