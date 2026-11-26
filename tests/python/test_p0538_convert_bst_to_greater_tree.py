from itertools import combinations
import unittest

from python.p0538_convert_bst_to_greater_tree import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def immutable_bst_shapes(values):
    if not values:
        return [None]
    shapes = []
    for index, value in enumerate(values):
        for left in immutable_bst_shapes(values[:index]):
            for right in immutable_bst_shapes(values[index + 1:]):
                shapes.append((value, left, right))
    return shapes


def materialize(shape):
    if shape is None:
        return None
    value, left, right = shape
    return TreeNode(value, materialize(left), materialize(right))


def snapshot(root):
    pending = [] if root is None else [root]
    records = {}
    while pending:
        node = pending.pop()
        records[id(node)] = (node.val, id(node.left), id(node.right))
        if node.left is not None:
            pending.append(node.left)
        if node.right is not None:
            pending.append(node.right)
    return records


class OriginalKeyGreaterSumTests(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def check(self, root, reference=None):
        before = snapshot(root)
        if reference is None:
            expected = {identity: sum(other[0] for other in before.values() if other[0] >= record[0])
                        for identity, record in before.items()}
        else:
            expected = {identity: reference(record[0]) for identity, record in before.items()}
        self.assertIs(self.solver.convertBST(root), root)
        after = snapshot(root)
        self.assertEqual({identity: record[0] for identity, record in after.items()}, expected)
        self.assertEqual({identity: record[1:] for identity, record in after.items()},
                         {identity: record[1:] for identity, record in before.items()})
        self.assertTrue(all(type(record[0]) is int for record in after.values()))

    def test_all_small_signed_bst_shapes_against_original_value_definition(self):
        count = 0
        vocabulary = (-10000, -4, -1, 0, 2, 7, 10000)
        for size in range(7):
            for values in combinations(vocabulary, size):
                for shape in immutable_bst_shapes(values):
                    self.check(materialize(shape))
                    count += 1
        self.assertEqual(count, 2521)

    def test_maximum_depth_positive_and_negative_chains_original_edges_and_empty(self):
        root = TreeNode(1)
        current = root
        for value in range(2, 10001):
            current.right = TreeNode(value)
            current = current.right
        self.assertEqual(len(snapshot(root)), 10000)
        self.check(root, lambda value: (value + 10000) * (10001 - value) // 2)
        root = TreeNode(-1)
        current = root
        for value in range(-2, -10001, -1):
            current.left = TreeNode(value)
            current = current.left
        self.assertEqual(len(snapshot(root)), 10000)
        self.check(root, lambda value: -((-value) * (-value + 1) // 2))
        self.check(TreeNode(0, TreeNode(-10000), TreeNode(10000)))
        self.check(TreeNode(-5))
        self.check(None)


if __name__ == '__main__':
    unittest.main()
