import unittest
from functools import lru_cache

from python.p0105_build_tree_preorder_inorder import TreeNode, Solution


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


def structural_sequence(test, root):
    result, pending, visited = [], [root], set()
    while pending:
        node = pending.pop()
        if node is None:
            result.append(None)
            continue
        test.assertNotIn(id(node), visited)
        visited.add(id(node))
        result.append(node.val)
        pending.extend([node.right, node.left])
    return result


class BuildTreeTests(unittest.TestCase):
    def check(self, expected_tree):
        expected = structural_sequence(self, expected_tree)
        preorder = [value for value in expected if value is not None]
        inorder = inorder_values(expected_tree)
        original_preorder, original_inorder = preorder[:], inorder[:]
        rebuilt = Solution().buildTree(preorder, inorder)
        self.assertEqual(structural_sequence(self, rebuilt), expected)
        self.assertEqual(preorder, original_preorder)
        self.assertEqual(inorder, original_inorder)

    def test_all_small_tree_shapes_against_structural_null_markers(self):
        checks = 0
        for size in range(8):
            for shape in shapes(size):
                self.check(build_tree(shape, range(size)))
                checks += 1
        self.assertEqual(checks, 626)

    def test_maximum_depth_both_directions_and_value_extremes(self):
        right = TreeNode(-1500)
        current = right
        for value in range(-1499, 1500):
            current.right = TreeNode(value)
            current = current.right
        self.check(right)
        left = TreeNode(1500)
        current = left
        for value in range(1499, -1500, -1):
            current.left = TreeNode(value)
            current = current.left
        self.check(left)
        self.check(TreeNode(0, TreeNode(-3000), TreeNode(3000)))
        self.check(TreeNode(7))
        self.check(None)


if __name__ == '__main__':
    unittest.main()
