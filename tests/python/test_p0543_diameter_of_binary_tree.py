import unittest
from collections import deque
from functools import lru_cache

from python.p0543_diameter_of_binary_tree import Solution


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
    return None if shape is None else Node(0, build(shape[0]), build(shape[1]))


def snapshot(root):
    records, pending = [], [root] if root else []
    while pending:
        node = pending.pop()
        records.append((node, node.val, node.left, node.right))
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return records


def all_pair_distances(root):
    adjacency = {}
    for node, _, left, right in snapshot(root):
        adjacency.setdefault(node, [])
        for child in (left, right):
            if child is not None:
                adjacency[node].append(child)
                adjacency.setdefault(child, []).append(node)
    farthest = 0
    for source in adjacency:
        pending, seen = deque([(source, 0)]), {source}
        while pending:
            node, distance = pending.popleft()
            farthest = max(farthest, distance)
            for neighbor in adjacency[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append((neighbor, distance + 1))
    return farthest


def chain(size, side):
    root = None
    for _ in range(size):
        node = Node(-100 if side == 'left' else 100)
        setattr(node, side, root)
        root = node
    return root


def perfect(levels):
    return None if not levels else Node(0, perfect(levels - 1), perfect(levels - 1))


class DiameterTests(unittest.TestCase):
    def check_tree(self, root, expected):
        before = snapshot(root)
        self.assertEqual(Solution().diameterOfBinaryTree(root), expected)
        for node, value, left, right in before:
            self.assertEqual(node.val, value)
            self.assertIs(node.left, left)
            self.assertIs(node.right, right)

    def test_all_small_shapes(self):
        checked = 0
        self.check_tree(None, 0)
        for size in range(1, 8):
            for shape in shapes(size):
                root = build(shape)
                self.check_tree(root, all_pair_distances(root))
                checked += 1
        self.assertEqual(checked, 625)

    def test_contract_boundaries(self):
        for side in ('left', 'right'):
            self.check_tree(chain(10000, side), 9999)
        self.check_tree(perfect(13), 24)
        junction = Node(0, chain(4, 'left'), chain(4, 'right'))
        self.check_tree(Node(100, junction), 8)
        self.check_tree(Node(-100), 0)


if __name__ == '__main__':
    unittest.main()
