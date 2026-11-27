from functools import lru_cache
from itertools import product
import unittest

from python.p0129_sum_root_to_leaf_numbers import TreeNode, Solution



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



def text_path_sum(node, prefix=''):
    text = prefix + str(node.val)
    if node.left is None and node.right is None:
        return int(text)
    return sum(text_path_sum(child, text) for child in (node.left, node.right)
               if child is not None)


class RootLeafDigitTests(unittest.TestCase):
    def check(self, root):
        before = tree_records(root)
        expected = text_path_sum(root)
        self.assertTrue(0 <= expected <= 2147483647)
        result = Solution().sumNumbers(root)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(tree_records(root), before)

    def test_all_small_digit_trees_against_string_paths(self):
        checks = 0
        for size in range(1, 6):
            for shape in shapes(size):
                for values in product((0, 2), repeat=size):
                    self.check(materialize(shape, values))
                    checks += 1
        self.assertEqual(checks, 1618)

    def test_maximum_nodes_depth_ten_leading_zero_and_digit_nine(self):
        nodes = [TreeNode(0) for _ in range(1000)]
        for index, node in enumerate(nodes):
            if 2 * index + 1 < len(nodes):
                node.left = nodes[2 * index + 1]
            if 2 * index + 2 < len(nodes):
                node.right = nodes[2 * index + 2]
            if node.left is None and node.right is None:
                node.val = 9
        self.check(nodes[0])
        for digits in ([1] + [0] * 9, list(range(10))):
            root = current = TreeNode(digits[0])
            for digit in digits[1:]:
                current.left = TreeNode(digit)
                current = current.left
            self.check(root)
        self.check(TreeNode(0))
        self.check(TreeNode(9))


if __name__ == '__main__':
    unittest.main()
