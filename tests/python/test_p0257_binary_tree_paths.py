from functools import lru_cache
from itertools import product
import unittest

from python.p0257_binary_tree_paths import TreeNode, Solution



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



def text_paths(node):
    if node.left is None and node.right is None:
        return [str(node.val)]
    return [str(node.val) + '->' + path for child in (node.left, node.right)
            if child is not None for path in text_paths(child)]


class RootLeafPathTextTests(unittest.TestCase):
    def check(self, root):
        before = tree_records(root)
        expected = text_paths(root)
        result = Solution().binaryTreePaths(root)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(path) is str for path in result))
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(tree_records(root), before)

    def test_all_small_trees_against_recursive_path_texts(self):
        checks = 0
        for size in range(1, 6):
            for shape in shapes(size):
                for values in product((-1, 0, 2), repeat=size):
                    self.check(materialize(shape, values))
                    checks += 1
        self.assertEqual(checks, 11496)

    def test_maximum_nodes_negative_text_and_duplicate_paths(self):
        root = current = TreeNode(-100)
        for index in range(1, 100):
            current.right = TreeNode(100 if index % 2 else -100)
            current = current.right
        self.check(root)
        nodes = [TreeNode(0) for _ in range(100)]
        for index, node in enumerate(nodes):
            if 2 * index + 1 < len(nodes):
                node.left = nodes[2 * index + 1]
            if 2 * index + 2 < len(nodes):
                node.right = nodes[2 * index + 2]
        self.check(nodes[0])
        self.check(TreeNode(-100, TreeNode(100), TreeNode(100)))


if __name__ == '__main__':
    unittest.main()
