import unittest
from functools import lru_cache
from itertools import product

from python.p0655_print_binary_tree import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for count in range(size) for left in shapes(count)
                 for right in shapes(size - count - 1))


def labeled(shape, values):
    if shape is None:
        return None
    value = next(values)
    return TreeNode(value, labeled(shape[0], values), labeled(shape[1], values))


def records(root):
    pending, result = [(root, 0, 0)], []
    while pending:
        node, depth, path = pending.pop()
        if node is not None:
            result.append((node, depth, path))
            pending.extend(((node.left, depth + 1, path * 2),
                            (node.right, depth + 1, path * 2 + 1)))
    return result


def path_formula(root):
    entries = records(root)
    rows = max((depth for _, depth, _ in entries), default=-1) + 1
    matrix = [[''] * ((1 << rows) - 1) for _ in range(rows)]
    for node, depth, path in entries:
        column = (2 * path + 1) * (1 << (rows - depth - 1)) - 1
        matrix[depth][column] = str(node.val)
    return matrix


def snapshot(root):
    return {id(node): (node.val, id(node.left), id(node.right)) for node, _, _ in records(root)}


def full(levels):
    return TreeNode(0, full(levels - 1), full(levels - 1)) if levels > 1 else TreeNode(0)


class PrintTreeTests(unittest.TestCase):
    def check(self, root):
        before = snapshot(root)
        actual = Solution().printTree(root)
        self.assertEqual(actual, path_formula(root))
        self.assertTrue(all(type(cell) is str for row in actual for cell in row))
        self.assertEqual(len({id(row) for row in actual}), len(actual))
        self.assertEqual(snapshot(root), before)
        return actual

    def test_all_small_labeled_trees_against_closed_form_path_columns(self):
        checked = 0
        for size in range(7):
            for shape in shapes(size):
                for values in product((-99, 99), repeat=size):
                    self.check(labeled(shape, iter(values)))
                    checked += 1
        self.assertEqual(checked, 10067)

    def test_ten_level_sparse_and_complete_trees_and_zero(self):
        for side in ('left', 'right'):
            root = None
            for depth in range(10):
                node = TreeNode(-99 if depth % 2 else 99)
                setattr(node, side, root)
                root = node
            result = self.check(root)
            self.assertEqual((len(result), len(result[0])), (10, 1023))
        result = self.check(full(10))
        self.assertEqual(sum(bool(cell) for row in result for cell in row), 1023)
        self.assertEqual(self.check(TreeNode(0)), [['0']])


if __name__ == '__main__':
    unittest.main()
