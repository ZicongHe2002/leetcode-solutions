import unittest
from functools import lru_cache
from itertools import product

from python.p0098_validate_binary_search_tree import TreeNode, Solution


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right)
                 for left_size in range(size)
                 for left in shapes(left_size)
                 for right in shapes(size - 1 - left_size))


def build_tree(shape, values):
    remaining = iter(values)

    def build(current):
        if current is None:
            return None
        node = TreeNode(next(remaining))
        node.left = build(current[0])
        node.right = build(current[1])
        return node

    return build(shape)


def snapshot(root):
    records = []
    pending = [root] if root is not None else []
    while pending:
        node = pending.pop()
        records.append((node, node.val, node.left, node.right))
        if node.right is not None:
            pending.append(node.right)
        if node.left is not None:
            pending.append(node.left)
    return records


def assert_unchanged(test, records):
    for node, value, left, right in records:
        test.assertEqual(node.val, value)
        test.assertIs(node.left, left)
        test.assertIs(node.right, right)


def inorder_values(root):
    result, pending = [], []
    current = root
    while current is not None or pending:
        while current is not None:
            pending.append(current)
            current = current.left
        current = pending.pop()
        result.append(current.val)
        current = current.right
    return result


class ValidateBSTTests(unittest.TestCase):
    def check(self, root):
        before = snapshot(root)
        values = inorder_values(root)
        expected = all(left < right for left, right in zip(values, values[1:]))
        result = Solution().isValidBST(root)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        assert_unchanged(self, before)

    def test_all_small_shapes_and_values_against_strict_inorder(self):
        checks = 0
        for size in range(6):
            for shape in shapes(size):
                for values in product(range(-1, 2), repeat=size):
                    self.check(build_tree(shape, values))
                    checks += 1
        self.assertEqual(checks, 11497)

    def test_ancestor_constraints_extreme_values_and_maximum_depth(self):
        self.check(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))
        self.check(TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(4), TreeNode(8))))
        self.check(TreeNode(0, TreeNode(-(2**31)), TreeNode(2**31 - 1)))
        self.check(TreeNode(0, TreeNode(0)))
        root = TreeNode(0)
        current = root
        for value in range(1, 10000):
            current.right = TreeNode(value)
            current = current.right
        self.check(root)
        current.val = -1
        self.check(root)
        self.check(None)


if __name__ == '__main__':
    unittest.main()
