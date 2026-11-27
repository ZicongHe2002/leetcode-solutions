import unittest
from functools import lru_cache
from itertools import product

from python.p0742_closest_leaf_in_a_binary_tree import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for split in range(size)
                 for left, right in product(shapes(split), shapes(size - split - 1)))


def build(shape, labels):
    if shape is None:
        return None
    node = TreeNode(next(labels))
    node.left, node.right = build(shape[0], labels), build(shape[1], labels)
    return node


def snapshot(root):
    result, stack = {}, [root]
    while stack:
        node = stack.pop()
        assert id(node) not in result
        result[id(node)] = (node.val, id(node.left) if node.left else None, id(node.right) if node.right else None)
        stack.extend(child for child in (node.left, node.right) if child is not None)
    return result


def root_path_nearest_leaves(root, target):
    paths, leaves, stack = {}, [], [(root, ())]
    while stack:
        node, prefix = stack.pop()
        path = prefix + (node.val,)
        paths[node.val] = path
        if node.left is None and node.right is None:
            leaves.append(node.val)
        stack.extend((child, path) for child in (node.left, node.right) if child is not None)
    distances = {}
    for leaf in leaves:
        left, right, common = paths[target], paths[leaf], 0
        for a, b in zip(left, right):
            if a != b:
                break
            common += 1
        distances[leaf] = len(left) + len(right) - 2 * common
    minimum = min(distances.values())
    return {leaf for leaf, distance in distances.items() if distance == minimum}


class ClosestLeafTests(unittest.TestCase):
    def check(self, root, target, expected=None):
        before = snapshot(root)
        expected = root_path_nearest_leaves(root, target) if expected is None else expected
        result = Solution().findClosestLeaf(root, target)
        self.assertIs(type(result), int)
        self.assertIn(result, expected)
        self.assertEqual(snapshot(root), before)

    def test_all_small_ordered_trees_and_targets_against_root_path_distances(self):
        trees = queries = 0
        for size in range(1, 8):
            for shape in shapes(size):
                root = build(shape, iter(range(1, size + 1)))
                trees += 1
                for target in range(1, size + 1):
                    self.check(root, target)
                    queries += 1
        self.assertEqual((trees, queries), (625, 4081))

    def test_ties_ancestor_shortcut_false_root_leaf_and_thousand_node_chains(self):
        self.check(TreeNode(1, TreeNode(2), TreeNode(3)), 1, {2, 3})
        self.check(TreeNode(1), 1, {1})
        self.check(TreeNode(1, TreeNode(2, TreeNode(3))), 2, {3})
        root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5, TreeNode(6)))), TreeNode(3))
        self.check(root, 2, {3})
        for side in ('left', 'right'):
            root = node = TreeNode(1)
            for value in range(2, 1001):
                child = TreeNode(value)
                setattr(node, side, child)
                node = child
            for target in (1, 500, 1000):
                self.check(root, target, {1000})


if __name__ == '__main__':
    unittest.main()
