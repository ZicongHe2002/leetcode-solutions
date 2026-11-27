from functools import lru_cache
from itertools import product
import unittest

from python.p0124_binary_tree_maximum_path_sum import TreeNode, Solution



@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in shapes(left_size) for right in shapes(size - 1 - left_size))


def materialize(shape, values):
    values = iter(values)

    def build(current):
        if current is None:
            return None
        node = TreeNode(next(values))
        node.left = build(current[0])
        node.right = build(current[1])
        return node

    return build(shape)



def tree_records(root):
    records = {}
    pending = [root] if root is not None else []
    while pending:
        node = pending.pop()
        if node in records:
            raise AssertionError('cycle or shared input node')
        records[node] = (node.val, node.left, node.right)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return records



def all_simple_paths(root):
    adjacency = {}
    pending = [(root, None)]
    while pending:
        node, parent = pending.pop()
        adjacency[node] = []
        if parent is not None:
            adjacency[parent].append(node)
            adjacency[node].append(parent)
        for child in (node.left, node.right):
            if child is not None:
                pending.append((child, node))
    best = float('-inf')
    for start in adjacency:
        pending = [(start, None, 0)]
        while pending:
            node, parent, total = pending.pop()
            total += node.val
            best = max(best, total)
            pending.extend((neighbor, node, total) for neighbor in adjacency[node]
                           if neighbor is not parent)
    return best


class NonemptyTreePathTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = tree_records(root)
        if expected is None:
            expected = all_simple_paths(root)
        result = Solution().maxPathSum(root)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(tree_records(root), before)

    def test_all_small_trees_against_all_undirected_simple_paths(self):
        checks = 0
        for size in range(1, 6):
            for shape in shapes(size):
                for values in product((-1, 0, 2), repeat=size):
                    self.check(materialize(shape, values))
                    checks += 1
        self.assertEqual(checks, 11496)

    def test_maximum_depth_positive_negative_and_path_below_root(self):
        for value, expected in ((1000, 30000000), (-1000, -1000)):
            root = current = TreeNode(value)
            for _ in range(29999):
                current.right = TreeNode(value)
                current = current.right
            self.check(root, expected)
        root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.check(root, 42)


if __name__ == '__main__':
    unittest.main()
