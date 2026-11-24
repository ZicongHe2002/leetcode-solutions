import unittest
from functools import lru_cache

from python.p0110_balanced_binary_tree import Solution


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.val, self.left, self.right = value, left, right


@lru_cache(None)
def shapes(size):
    if not size:
        return (None,)
    return tuple((left, right) for split in range(size)
                 for left in shapes(split) for right in shapes(size - split - 1))


def build(shape):
    return None if shape is None else Node(0, build(shape[0]), build(shape[1]))


def height(root):
    return 0 if root is None else 1 + max(height(root.left), height(root.right))


def oracle(root):
    return root is None or (abs(height(root.left) - height(root.right)) <= 1
                            and oracle(root.left) and oracle(root.right))


def snapshot(root):
    pending = [root] if root else []
    records = []
    while pending:
        node = pending.pop()
        records.append((node, node.val, node.left, node.right))
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return records


def chain(size, side):
    root = None
    for _ in range(size):
        parent = Node(-10000 if side == 'left' else 10000)
        setattr(parent, side, root)
        root = parent
    return root


def perfect(levels):
    if not levels:
        return None
    return Node(10000, perfect(levels - 1), perfect(levels - 1))


class BalancedTreeTests(unittest.TestCase):
    def check_tree(self, root, expected):
        before = snapshot(root)
        self.assertIs(Solution().isBalanced(root), expected)
        for node, value, left, right in before:
            self.assertEqual(node.val, value)
            self.assertIs(node.left, left)
            self.assertIs(node.right, right)

    def test_all_small_shapes(self):
        checked = 0
        for size in range(8):
            for shape in shapes(size):
                root = build(shape)
                self.check_tree(root, oracle(root))
                checked += 1
        self.assertEqual(checked, 626)

    def test_contract_boundaries(self):
        for side in ('left', 'right'):
            self.check_tree(chain(5000, side), False)
        self.check_tree(perfect(12), True)
        root = Node(0, chain(3, 'left'), chain(3, 'right'))
        self.assertEqual(height(root.left), height(root.right))
        self.check_tree(root, False)
        self.check_tree(Node(-10000, Node(10000)), True)
        self.check_tree(Node(10000), True)


if __name__ == '__main__':
    unittest.main()
