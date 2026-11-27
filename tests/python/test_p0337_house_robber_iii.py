from collections import deque
from functools import lru_cache
from itertools import product
import unittest

from python.p0337_house_robber_iii import Solution, TreeNode


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in shapes(left_size) for right in shapes(size - 1 - left_size))


def build_shape(shape, values):
    source = iter(values)
    def build(current):
        if current is None:
            return None
        return TreeNode(next(source), build(current[0]), build(current[1]))
    return build(shape)


def nodes_edges_snapshot(root):
    pending = deque([] if root is None else [(root, None)])
    nodes, edges, snapshot = [], [], []
    seen = set()
    while pending:
        node, parent = pending.popleft()
        if id(node) in seen:
            raise AssertionError('not a tree')
        seen.add(id(node))
        index = len(nodes)
        nodes.append(node)
        if parent is not None:
            edges.append((parent, index))
        snapshot.append((id(node), node.val, id(node.left) if node.left is not None else None, id(node.right) if node.right is not None else None))
        if node.left is not None:
            pending.append((node.left, index))
        if node.right is not None:
            pending.append((node.right, index))
    return nodes, edges, snapshot


def subset_oracle(nodes, edges):
    best = 0
    for mask in range(1 << len(nodes)):
        if any(mask & (1 << parent) and mask & (1 << child) for parent, child in edges):
            continue
        best = max(best, sum(node.val for index, node in enumerate(nodes) if mask & (1 << index)))
    return best


class TreeIndependentSetTests(unittest.TestCase):
    def check(self, root, expected=None):
        nodes, edges, before = nodes_edges_snapshot(root)
        expected = subset_oracle(nodes, edges) if expected is None else expected
        actual = Solution().rob(root)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected)
        self.assertEqual(nodes_edges_snapshot(root)[2], before)

    def test_all_small_tree_shapes_and_labels_against_all_house_subsets(self):
        trees = 0
        for size in range(6):
            for shape in shapes(size):
                for values in product((0, 1, 2), repeat=size):
                    self.check(build_shape(shape, values))
                    trees += 1
        self.assertEqual(trees, 11497)

    def test_grandchildren_deep_trees_maximum_values_and_call_isolation(self):
        self.check(TreeNode(4, TreeNode(1, TreeNode(5)), TreeNode(2)), 9)
        for direction, value in (('left', 1), ('right', 10000)):
            root = None
            for _ in range(10000):
                parent = TreeNode(value)
                setattr(parent, direction, root)
                root = parent
            self.check(root, 5000 * value)
        solver = Solution()
        self.assertEqual(solver.rob(None), 0)
        self.assertEqual(solver.rob(TreeNode(7)), 7)


if __name__ == '__main__':
    unittest.main()
