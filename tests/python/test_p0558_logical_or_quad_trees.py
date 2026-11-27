from itertools import product
from random import Random
import unittest

import python.p0558_logical_or_quad_trees as solution_module


FIELDS = ('topLeft', 'topRight', 'bottomLeft', 'bottomRight')


class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val, self.isLeaf = val, isLeaf
        self.topLeft, self.topRight = topLeft, topRight
        self.bottomLeft, self.bottomRight = bottomLeft, bottomRight


solution_module.Node = Node


def construct_from_grid(grid, row=0, column=0, size=None):
    if size is None:
        size = len(grid)
    first = grid[row][column]
    if all(grid[r][c] == first for r in range(row, row + size) for c in range(column, column + size)):
        return Node(bool(first), True)
    half = size // 2
    return Node(True, False,
                construct_from_grid(grid, row, column, half),
                construct_from_grid(grid, row, column + half, half),
                construct_from_grid(grid, row + half, column, half),
                construct_from_grid(grid, row + half, column + half, half))


def snapshot(root):
    pending, records = [root], {}
    while pending:
        node = pending.pop()
        if id(node) in records:
            raise AssertionError('Repeated node or cycle in an input tree')
        children = tuple(getattr(node, field) for field in FIELDS)
        records[id(node)] = (node.val, node.isLeaf, tuple(map(id, children)))
        if not node.isLeaf:
            pending.extend(children)
    return records


class QuadTreeBooleanGridTests(unittest.TestCase):
    def decode_and_validate(self, root, size):
        grid = [[None] * size for _ in range(size)]

        def fill(node, row, column, width):
            children = tuple(getattr(node, field) for field in FIELDS)
            if node.isLeaf:
                self.assertIn(node.val, (0, 1))
                self.assertTrue(all(child is None for child in children))
                for r in range(row, row + width):
                    for c in range(column, column + width):
                        grid[r][c] = int(bool(node.val))
                return
            self.assertGreater(width, 1)
            self.assertTrue(all(child is not None for child in children))
            half = width // 2
            for child, dr, dc in zip(children, (0, 0, half, half), (0, half, 0, half)):
                fill(child, row + dr, column + dc, half)
            self.assertTrue(any(grid[r][c] != grid[row][column]
                                for r in range(row, row + width) for c in range(column, column + width)))

        fill(root, 0, 0, size)
        return grid

    def check(self, first, second):
        left, right = construct_from_grid(first), construct_from_grid(second)
        before_left, before_right = snapshot(left), snapshot(right)
        actual = solution_module.Solution().intersect(left, right)
        expected = [[int(a or b) for a, b in zip(row_a, row_b)] for row_a, row_b in zip(first, second)]
        self.assertEqual(self.decode_and_validate(actual, len(first)), expected)
        self.assertEqual(snapshot(left), before_left)
        self.assertEqual(snapshot(right), before_right)

    def test_every_pair_of_one_and_two_cell_side_grids(self):
        pairs = 0
        for size in (1, 2):
            grids = [[list(bits[start:start + size]) for start in range(0, len(bits), size)]
                     for bits in product((0, 1), repeat=size * size)]
            for first in grids:
                for second in grids:
                    self.check(first, second)
                    pairs += 1
        self.assertEqual(pairs, 260)

    def test_deeper_fixed_seed_grids_maximum_structured_area_and_internal_placeholder_values(self):
        random = Random(558)
        for size in (4, 8, 16, 32):
            for _ in range(20):
                first = [[random.randrange(2) for _ in range(size)] for _ in range(size)]
                second = [[random.randrange(2) for _ in range(size)] for _ in range(size)]
                self.check(first, second)
        size = 512
        first = [[int(row < size // 2) for _ in range(size)] for row in range(size)]
        second = [[int(column < size // 2) for column in range(size)] for _ in range(size)]
        self.check(first, second)


if __name__ == '__main__':
    unittest.main()
