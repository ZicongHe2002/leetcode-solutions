from functools import lru_cache
from itertools import product
import unittest

from python.p0549_binary_tree_longest_consecutive_sequence_ii import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def immutable_shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in immutable_shapes(left_size)
                 for right in immutable_shapes(size - left_size - 1))


def materialize(shape, values):
    if shape is None:
        return None
    left, right = shape
    return TreeNode(next(values), materialize(left, values), materialize(right, values))


def snapshot_and_nodes(root):
    pending, records, nodes = [root], {}, []
    while pending:
        node = pending.pop()
        if id(node) in records:
            raise AssertionError('Repeated node or cycle')
        records[id(node)] = (node.val, id(node.left), id(node.right))
        nodes.append(node)
        if node.left is not None:
            pending.append(node.left)
        if node.right is not None:
            pending.append(node.right)
    return records, nodes


def all_undirected_paths_oracle(root):
    _, nodes = snapshot_and_nodes(root)
    adjacent = {id(node): [] for node in nodes}
    for node in nodes:
        for child in (node.left, node.right):
            if child is not None:
                adjacent[id(node)].append(child)
                adjacent[id(child)].append(node)
    answer = 1
    for start in nodes:
        pending = [(start, None, ())]
        while pending:
            node, parent, values = pending.pop()
            values = values + (node.val,)
            differences = [right - left for left, right in zip(values, values[1:])]
            if all(step == 1 for step in differences) or all(step == -1 for step in differences):
                answer = max(answer, len(values))
            for neighbor in adjacent[id(node)]:
                if neighbor is not parent:
                    pending.append((neighbor, node, values))
    return answer


class BidirectionalConsecutiveArmTests(unittest.TestCase):
    def check(self, root, expected=None):
        before, _ = snapshot_and_nodes(root)
        actual = Solution().longestConsecutive(root)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, all_undirected_paths_oracle(root) if expected is None else expected)
        after, _ = snapshot_and_nodes(root)
        self.assertEqual(after, before)

    def test_all_small_shapes_and_signed_labels_against_every_undirected_path(self):
        trees = 0
        for size in range(1, 6):
            for shape in immutable_shapes(size):
                for values in product((-1, 0, 1), repeat=size):
                    self.check(materialize(shape, iter(values)))
                    trees += 1
        self.assertEqual(trees, 11496)

    def test_maximum_depth_alternating_direction_root_crossing_and_value_limits(self):
        root = TreeNode(0)
        node = root
        for value in range(1, 30000):
            node.right = TreeNode(value)
            node = node.right
        self.assertEqual(len(snapshot_and_nodes(root)[1]), 30000)
        self.check(root, 30000)
        root = TreeNode(0)
        node = root
        for index in range(1, 30000):
            node.right = TreeNode(index % 2)
            node = node.right
        self.check(root, 2)
        root = TreeNode(0)
        node = root
        for value in range(-1, -15001, -1):
            node.left = TreeNode(value)
            node = node.left
        node = root
        for value in range(1, 15000):
            node.right = TreeNode(value)
            node = node.right
        self.assertEqual(len(snapshot_and_nodes(root)[1]), 30000)
        self.check(root, 30000)
        self.check(TreeNode(0, TreeNode(-30000), TreeNode(30000)), 1)
        self.check(TreeNode(2, TreeNode(1), TreeNode(3)), 3)
        self.check(TreeNode(1, TreeNode(2), TreeNode(3)), 2)


if __name__ == '__main__':
    unittest.main()
