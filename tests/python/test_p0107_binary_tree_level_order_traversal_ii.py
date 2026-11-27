import unittest
from functools import lru_cache

from python.p0107_binary_tree_level_order_traversal_ii import Solution, TreeNode


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right)
                 for left_size in range(size)
                 for left in shapes(left_size)
                 for right in shapes(size - left_size - 1))


def build_tree(shape, values):
    remaining = iter(values)

    def build(current):
        if current is None:
            return None
        return TreeNode(next(remaining), build(current[0]), build(current[1]))

    return build(shape)


class BottomUpLevelsTests(unittest.TestCase):
    def check(self, root):
        expected, records = [], []
        pending = [(root, 0)] if root is not None else []
        while pending:
            node, depth = pending.pop()
            records.append((node, node.val, node.left, node.right))
            if depth == len(expected):
                expected.append([])
            expected[depth].append(node.val)
            if node.right is not None:
                pending.append((node.right, depth + 1))
            if node.left is not None:
                pending.append((node.left, depth + 1))
        result = Solution().levelOrderBottom(root)
        self.assertEqual(result, list(reversed(expected)))
        self.assertEqual(len({id(layer) for layer in result}), len(result))
        for node, value, left, right in records:
            self.assertEqual(node.val, value)
            self.assertIs(node.left, left)
            self.assertIs(node.right, right)

    def test_all_small_shapes_against_depth_first_buckets(self):
        checks = 0
        for size in range(9):
            for shape in shapes(size):
                self.check(build_tree(shape, range(size)))
                checks += 1
        self.assertEqual(checks, 2056)

    def test_maximum_depth_width_gaps_and_extreme_values(self):
        root = TreeNode(-1000)
        current = root
        for index in range(1999):
            child = TreeNode(index % 7 - 3)
            if index % 2:
                current.right = child
            else:
                current.left = child
            current = child
        self.check(root)
        nodes = [TreeNode(index % 11 - 5) for index in range(2000)]
        for index, node in enumerate(nodes):
            if 2 * index + 1 < len(nodes):
                node.left = nodes[2 * index + 1]
            if 2 * index + 2 < len(nodes):
                node.right = nodes[2 * index + 2]
        self.check(nodes[0])
        self.check(TreeNode(1000, TreeNode(-1000, None, TreeNode(0)), TreeNode(1)))
        self.check(TreeNode(0, TreeNode(0), TreeNode(0)))


if __name__ == '__main__':
    unittest.main()
