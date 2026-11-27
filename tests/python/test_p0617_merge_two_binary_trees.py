from functools import lru_cache
from itertools import product
import unittest

from python import p0617_merge_two_binary_trees as solution_module


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for k in range(size)
                 for left in shapes(k) for right in shapes(size - 1 - k))


def materialize(shape, values):
    if shape is None:
        return None
    node = TreeNode(next(values))
    node.left = materialize(shape[0], values)
    node.right = materialize(shape[1], values)
    return node


def snapshot(root):
    pending = [] if root is None else [root]
    records = {}
    while pending:
        node = pending.pop()
        if node in records:
            raise AssertionError('A tree must not contain cycles or shared child nodes')
        records[node] = (node.val, node.left, node.right)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return records


def path_values(root):
    pending = [] if root is None else [(root, '')]
    values = {}
    while pending:
        node, path = pending.pop()
        values[path] = node.val
        if node.left is not None:
            pending.append((node.left, path + 'L'))
        if node.right is not None:
            pending.append((node.right, path + 'R'))
    return values


def chain(size, value, side='left'):
    root = None
    for _ in range(size):
        node = TreeNode(value)
        setattr(node, side, root)
        root = node
    return root


class MergeBinaryTreesTests(unittest.TestCase):
    def setUp(self):
        solution_module.TreeNode = TreeNode

    def check(self, first, second):
        before_first, before_second = snapshot(first), snapshot(second)
        a, b = path_values(first), path_values(second)
        expected = {path: a.get(path, 0) + b.get(path, 0) for path in a.keys() | b.keys()}
        result = solution_module.Solution().mergeTrees(first, second)
        if expected:
            self.assertIsInstance(result, TreeNode)
        else:
            self.assertIsNone(result)
        result_nodes = snapshot(result)
        self.assertEqual(path_values(result), expected)
        self.assertFalse(set(result_nodes).intersection(before_first))
        self.assertFalse(set(result_nodes).intersection(before_second))
        self.assertEqual(snapshot(first), before_first)
        self.assertEqual(snapshot(second), before_second)
        return result

    def test_all_small_labeled_tree_pairs_against_path_value_union(self):
        trees = [materialize(shape, iter(labels)) for size in range(4) for shape in shapes(size)
                 for labels in product((-1, 0, 2), repeat=size)]
        self.assertEqual(len(trees), 157)
        cases = 0
        for first in trees:
            for second in trees:
                self.check(first, second)
                cases += 1
        self.assertEqual(cases, 24649)

    def test_two_thousand_depth_signed_values_disjoint_branches_and_sample(self):
        self.check(chain(2000, 10000), chain(2000, 10000))
        self.check(chain(2000, 10000), chain(2000, -10000))
        first = TreeNode(10000, chain(1999, 10000))
        second = TreeNode(-10000, None, chain(1999, -10000, 'right'))
        result = self.check(first, second)
        self.assertEqual(len(snapshot(result)), 3999)
        self.check(TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
                   TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7))))


if __name__ == '__main__':
    unittest.main()
