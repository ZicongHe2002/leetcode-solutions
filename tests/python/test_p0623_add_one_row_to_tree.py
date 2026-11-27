from functools import lru_cache
from itertools import count, cycle
import unittest

from python import p0623_add_one_row_to_tree as solution_module


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for k in range(size)
                 for left in shapes(k) for right in shapes(size - 1 - k))


def height(shape):
    return 0 if shape is None else 1 + max(height(shape[0]), height(shape[1]))


def materialize(shape, values):
    if shape is None:
        return None
    node = TreeNode(next(values))
    node.left = materialize(shape[0], values)
    node.right = materialize(shape[1], values)
    return node


def nodes_by_path(root):
    pending, nodes, seen = [(root, '')], {}, set()
    while pending:
        node, path = pending.pop()
        if node in seen:
            raise AssertionError('Cycles or shared children are not a tree')
        seen.add(node)
        nodes[path] = node
        if node.left is not None:
            pending.append((node.left, path + 'L'))
        if node.right is not None:
            pending.append((node.right, path + 'R'))
    return nodes


class AddTreeRowTests(unittest.TestCase):
    def setUp(self):
        solution_module.TreeNode = TreeNode

    def check(self, root, val, depth):
        old = nodes_by_path(root)
        before = {node: (node.val, node.left, node.right) for node in old.values()}
        expected = {}
        shifted = {}
        for path, node in old.items():
            if depth == 1:
                new_path = 'L' + path
            elif len(path) >= depth - 1:
                new_path = path[:depth - 2] + path[depth - 2] + path[depth - 2:]
            else:
                new_path = path
            expected[new_path] = node.val
            shifted[new_path] = node
        parents = {node for path, node in old.items() if len(path) == depth - 2} if depth > 1 else set()
        if depth == 1:
            expected[''] = val
        else:
            for path in old:
                if len(path) == depth - 2:
                    expected[path + 'L'] = expected[path + 'R'] = val
        result = solution_module.Solution().addOneRow(root, val, depth)
        actual = nodes_by_path(result)
        self.assertEqual({path: node.val for path, node in actual.items()}, expected)
        self.assertEqual(len(actual), len({id(node) for node in actual.values()}))
        for path, node in shifted.items():
            self.assertIs(actual[path], node)
        self.assertEqual(len(set(actual.values()) - set(before)), 1 if depth == 1 else 2 * len(parents))
        for node, (old_val, old_left, old_right) in before.items():
            self.assertEqual(node.val, old_val)
            if node not in parents:
                self.assertIs(node.left, old_left)
                self.assertIs(node.right, old_right)
            else:
                self.assertIs(node.left.left, old_left)
                self.assertIsNone(node.left.right)
                self.assertIsNone(node.right.left)
                self.assertIs(node.right.right, old_right)
        if depth == 1:
            self.assertIs(result.left, root)
            self.assertIsNone(result.right)
        else:
            self.assertIs(result, root)
        return result

    def test_every_small_shape_all_legal_depths_labels_and_inserted_value_bounds(self):
        trees = 0
        for size in range(1, 8):
            for shape in shapes(size):
                trees += 1
                for depth in range(1, height(shape) + 2):
                    for repeated in (False, True):
                        for val in (-100000, 100000):
                            root = materialize(shape, cycle((-100, 0, 100)) if repeated else count())
                            self.check(root, val, depth)
        self.assertEqual(trees, 625)

    def test_ten_thousand_depth_and_wide_last_row(self):
        self.check(TreeNode(0), 0, 1)
        self.check(TreeNode(0), 0, 2)
        nodes = [TreeNode(1) for _ in range(10000)]
        for parent, child in zip(nodes, nodes[1:]):
            parent.left = child
        result = solution_module.Solution().addOneRow(nodes[0], 100000, 10001)
        self.assertIs(result, nodes[0])
        for index, node in enumerate(nodes):
            self.assertEqual(node.val, 1)
            if index < 9999:
                self.assertIs(node.left, nodes[index + 1])
                self.assertIsNone(node.right)
        leaf = nodes[-1]
        self.assertIsNot(leaf.left, leaf.right)
        self.assertNotIn(leaf.left, nodes)
        self.assertNotIn(leaf.right, nodes)
        for child in (leaf.left, leaf.right):
            self.assertEqual(child.val, 100000)
            self.assertIsNone(child.left)
            self.assertIsNone(child.right)
        wide = [TreeNode(index % 201 - 100) for index in range(8191)]
        for index, node in enumerate(wide):
            if 2 * index + 2 < len(wide):
                node.left, node.right = wide[2 * index + 1], wide[2 * index + 2]
        result = self.check(wide[0], -100000, 14)
        self.assertEqual(len(nodes_by_path(result)), 16383)


if __name__ == '__main__':
    unittest.main()
