import unittest
from functools import lru_cache

from python.p0144_binary_tree_preorder_traversal import TreeNode, Solution


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


class PreorderTests(unittest.TestCase):
    def check(self, root, expected):
        before = snapshot(root)
        self.assertEqual(Solution().preorderTraversal(root), list(expected))
        assert_unchanged(self, before)

    def test_all_small_tree_shapes_against_construction_labels(self):
        checks = 0
        for size in range(9):
            for shape in shapes(size):
                values = list(range(size))
                self.check(build_tree(shape, values), values)
                checks += 1
        self.assertEqual(checks, 2056)

    def test_maximum_depth_complete_tree_repeated_and_extreme_values(self):
        root = TreeNode(-100)
        current = root
        for index in range(1, 100):
            child = TreeNode(100)
            if index % 2:
                current.left = child
            else:
                current.right = child
            current = child
        self.check(root, [-100] + [100] * 99)
        nodes = [TreeNode(0) for _ in range(100)]
        for index in range(100):
            if 2 * index + 1 < 100:
                nodes[index].left = nodes[2 * index + 1]
            if 2 * index + 2 < 100:
                nodes[index].right = nodes[2 * index + 2]
        self.check(nodes[0], [0] * 100)
        self.check(None, [])


if __name__ == '__main__':
    unittest.main()
