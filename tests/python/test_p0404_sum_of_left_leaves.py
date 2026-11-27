from functools import lru_cache
from itertools import product
import unittest

from python.p0404_sum_of_left_leaves import TreeNode, Solution



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



def parent_left_leaf_sum(node):
    own = 0
    if node.left is not None and node.left.left is None and node.left.right is None:
        own = node.left.val
    return own + sum(parent_left_leaf_sum(child) for child in (node.left, node.right)
                     if child is not None)


class LeftLeafDirectionTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = tree_records(root)
        if expected is None:
            expected = parent_left_leaf_sum(root)
        result = Solution().sumOfLeftLeaves(root)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(tree_records(root), before)

    def test_all_small_trees_against_parent_child_inspection(self):
        checks = 0
        for size in range(1, 6):
            for shape in shapes(size):
                for values in product((-1, 0, 2), repeat=size):
                    self.check(materialize(shape, values))
                    checks += 1
        self.assertEqual(checks, 11496)

    def test_maximum_nodes_leaf_direction_root_and_value_limits(self):
        for side in ('left', 'right'):
            root = current = TreeNode(1000)
            for _ in range(999):
                child = TreeNode(1000)
                setattr(current, side, child)
                current = child
            current.val = -1000
            self.check(root, -1000 if side == 'left' else 0)
        nodes = [TreeNode(10) for _ in range(1000)]
        for index, node in enumerate(nodes):
            if 2 * index + 1 < len(nodes):
                node.left = nodes[2 * index + 1]
            if 2 * index + 2 < len(nodes):
                node.right = nodes[2 * index + 2]
        expected = sum(10 for index in range(1, 1000, 2) if 2 * index + 1 >= 1000)
        self.check(nodes[0], expected)
        self.check(TreeNode(1000), 0)


if __name__ == '__main__':
    unittest.main()
