import unittest
from collections import deque
from functools import lru_cache
from itertools import product

from python.p0199_binary_tree_right_side_view import TreeNode, Solution


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


class RightSideViewTests(unittest.TestCase):
    def check(self, root):
        before = snapshot(root)
        expected = []
        pending = deque([root] if root is not None else [])
        while pending:
            layer = [pending.popleft() for _ in range(len(pending))]
            expected.append(layer[-1].val)
            for node in layer:
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
        self.assertEqual(Solution().rightSideView(root), expected)
        assert_unchanged(self, before)

    def test_all_small_shapes_and_values_against_last_breadth_first_node(self):
        checks = 0
        for size in range(7):
            for shape in shapes(size):
                for values in product((-1, 1), repeat=size):
                    self.check(build_tree(shape, values))
                    checks += 1
        self.assertEqual(checks, 10067)

    def test_left_deeper_gaps_complete_tree_and_maximum_depth(self):
        self.check(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4)))
        root = TreeNode(-100)
        current = root
        for index in range(1, 100):
            child = TreeNode(100 if index % 2 else -100)
            if index % 2:
                current.left = child
            else:
                current.right = child
            current = child
        self.check(root)
        nodes = [TreeNode(index - 50) for index in range(100)]
        for index in range(100):
            if 2 * index + 1 < 100:
                nodes[index].left = nodes[2 * index + 1]
            if 2 * index + 2 < 100:
                nodes[index].right = nodes[2 * index + 2]
        self.check(nodes[0])
        self.check(None)


if __name__ == '__main__':
    unittest.main()
