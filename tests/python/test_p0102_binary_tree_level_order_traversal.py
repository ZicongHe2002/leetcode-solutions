import unittest
from functools import lru_cache
from itertools import product

from python.p0102_binary_tree_level_order_traversal import TreeNode, Solution


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


class LevelOrderTests(unittest.TestCase):
    def check(self, root):
        before = snapshot(root)
        expected = []
        pending = [(root, 0)] if root is not None else []
        while pending:
            node, depth = pending.pop()
            if depth == len(expected):
                expected.append([])
            expected[depth].append(node.val)
            if node.right is not None:
                pending.append((node.right, depth + 1))
            if node.left is not None:
                pending.append((node.left, depth + 1))
        result = Solution().levelOrder(root)
        self.assertEqual(result, expected)
        self.assertEqual(len({id(layer) for layer in result}), len(result))
        assert_unchanged(self, before)

    def test_all_small_shapes_and_values_against_depth_first_buckets(self):
        checks = 0
        for size in range(7):
            for shape in shapes(size):
                for values in product((-1, 1), repeat=size):
                    self.check(build_tree(shape, values))
                    checks += 1
        self.assertEqual(checks, 10067)

    def test_maximum_depth_width_gaps_and_value_extremes(self):
        root = TreeNode(-1000)
        current = root
        for _ in range(1999):
            current.left = TreeNode(1000)
            current = current.left
        self.check(root)
        nodes = [TreeNode(index % 2001 - 1000) for index in range(2000)]
        for index in range(2000):
            if 2 * index + 1 < 2000:
                nodes[index].left = nodes[2 * index + 1]
            if 2 * index + 2 < 2000:
                nodes[index].right = nodes[2 * index + 2]
        self.check(nodes[0])
        self.check(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)))
        self.check(None)


if __name__ == '__main__':
    unittest.main()
