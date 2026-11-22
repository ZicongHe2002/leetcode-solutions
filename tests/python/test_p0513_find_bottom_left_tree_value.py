from functools import lru_cache
import unittest

from python.p0513_find_bottom_left_tree_value import Solution, TreeNode



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



def left_first_depth_oracle(root):
    deepest, answer = -1, None
    pending = [(root, 0)]
    while pending:
        node, depth = pending.pop()
        if depth > deepest:
            deepest, answer = depth, node.val
        if node.right is not None:
            pending.append((node.right, depth + 1))
        if node.left is not None:
            pending.append((node.left, depth + 1))
    return answer


class BottomLeftDepthOracleTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = tree_records(root)
        if expected is None:
            expected = left_first_depth_oracle(root)
        result = Solution().findBottomLeftValue(root)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(tree_records(root), before)

    def test_all_small_shapes_against_left_first_depth_search(self):
        checked = 0
        for size in range(1, 8):
            for shape in shapes(size):
                self.check(materialize(shape, range(-size, 0)))
                checked += 1
        self.assertEqual(checked, 625)

    def test_maximum_node_count_deep_and_wide_trees_value_endpoints(self):
        root = current = TreeNode(-5000)
        for value in range(-4999, 5000):
            current.right = TreeNode(value)
            current = current.right
        self.check(root, 4999)
        nodes = [TreeNode(index - 5000) for index in range(10000)]
        for index, node in enumerate(nodes):
            if 2 * index + 1 < len(nodes):
                node.left = nodes[2 * index + 1]
            if 2 * index + 2 < len(nodes):
                node.right = nodes[2 * index + 2]
        self.check(nodes[0], 8191 - 5000)
        self.check(TreeNode(-2**31), -2**31)
        self.check(TreeNode(2**31 - 1, TreeNode(-2**31)), -2**31)


if __name__ == '__main__':
    unittest.main()
