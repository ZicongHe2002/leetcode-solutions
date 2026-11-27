from functools import lru_cache
from itertools import product
import unittest

from python.p0113_path_sum_ii import Solution, TreeNode



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



def leaf_paths_from_parents(root):
    if root is None:
        return []
    parents, leaves, pending = {root: None}, [], [root]
    while pending:
        node = pending.pop()
        if node.left is None and node.right is None:
            leaves.append(node)
        for child in (node.left, node.right):
            if child is not None:
                parents[child] = node
                pending.append(child)
    result = []
    for leaf in leaves:
        path = []
        node = leaf
        while node is not None:
            path.append(node.val)
            node = parents[node]
        result.append(list(reversed(path)))
    return result


class PathSumParentOracleTests(unittest.TestCase):
    def check(self, root, target):
        before = tree_records(root)
        expected = [tuple(path) for path in leaf_paths_from_parents(root) if sum(path) == target]
        result = Solution().pathSum(root, target)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(path) is list and all(type(value) is int for value in path)
                            for path in result))
        self.assertEqual(sorted(tuple(path) for path in result), sorted(expected))
        self.assertEqual(tree_records(root), before)

    def test_all_small_shapes_values_and_targets_against_leaf_parents(self):
        trees = checks = 0
        for size in range(6):
            for shape in shapes(size):
                for values in product((-1, 0, 1), repeat=size):
                    root = materialize(shape, values)
                    trees += 1
                    for target in (-2, -1, 0, 1, 2):
                        self.check(root, target)
                        checks += 1
        self.assertEqual((trees, checks), (11497, 57485))

    def test_maximum_depth_signed_values_and_duplicate_value_paths(self):
        for alternating in (False, True):
            root = current = TreeNode(1 if alternating else 0)
            for index in range(1, 5000):
                current.left = TreeNode((-1 if index % 2 else 1) if alternating else 0)
                current = current.left
            self.check(root, 0)
        self.check(TreeNode(1, TreeNode(-1), TreeNode(-1)), 0)
        self.check(TreeNode(1000, TreeNode(-1000)), 0)
        self.check(TreeNode(-1000), -1000)
        self.check(TreeNode(1000), 1000)


if __name__ == '__main__':
    unittest.main()
