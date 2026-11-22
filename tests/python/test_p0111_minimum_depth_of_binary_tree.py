import unittest
from collections import deque
from functools import lru_cache

from python.p0111_minimum_depth_of_binary_tree import Solution


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.val, self.left, self.right = value, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for split in range(size)
                 for left in shapes(split) for right in shapes(size - split - 1))


def build(shape):
    if shape is None:
        return None
    return Node(0, build(shape[0]), build(shape[1]))


def snapshot(root):
    pending = [root] if root else []
    result = []
    while pending:
        node = pending.pop()
        result.append((node, node.val, node.left, node.right))
        if node.left:
            pending.append(node.left)
        if node.right:
            pending.append(node.right)
    return result


def path_lengths(node):
    if node.left is None and node.right is None:
        return [1]
    return [length + 1 for child in (node.left, node.right) if child is not None
            for length in path_lengths(child)]


def chain(size, side):
    root = None
    for _ in range(size):
        node = Node(-1000 if side == 'left' else 1000)
        setattr(node, side, root)
        root = node
    return root


class MinimumDepthTests(unittest.TestCase):
    def check_tree(self, root, expected):
        before = snapshot(root)
        self.assertEqual(Solution().minDepth(root), expected)
        for node, value, left, right in before:
            self.assertEqual(node.val, value)
            self.assertIs(node.left, left)
            self.assertIs(node.right, right)

    def test_all_small_shapes(self):
        checked = 0
        for size in range(8):
            for shape in shapes(size):
                root = build(shape)
                self.check_tree(root, min(path_lengths(root)) if root else 0)
                checked += 1
        self.assertEqual(checked, 626)

    def test_contract_boundaries(self):
        for side in ('left', 'right'):
            self.check_tree(chain(100000, side), 100000)
        root = Node()
        pending = deque([(root, 1)])
        while pending:
            node, depth = pending.popleft()
            if depth < 16:
                node.left, node.right = Node(-1000), Node(1000)
                pending.extend(((node.left, depth + 1), (node.right, depth + 1)))
        self.check_tree(root, 16)
        self.check_tree(Node(0, Node(-1000), chain(99998, 'right')), 2)
        self.check_tree(Node(1000), 1)


if __name__ == '__main__':
    unittest.main()
