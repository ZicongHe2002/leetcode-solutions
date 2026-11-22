from functools import lru_cache
from itertools import combinations
import unittest

from python.p0099_recover_binary_search_tree import Solution, TreeNode



@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in shapes(left_size) for right in shapes(size - 1 - left_size))



def bst_from_shape(shape, values):
    values = iter(values)

    def build(current):
        if current is None:
            return None
        left = build(current[0])
        node = TreeNode(next(values))
        node.left = left
        node.right = build(current[1])
        return node

    return build(shape)


def inorder_nodes(root):
    result, stack = [], []
    current = root
    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current)
        current = current.right
    return result



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



class RecoverBSTOriginalIdentityTests(unittest.TestCase):
    def check_swap(self, root, nodes, before, first, second):
        nodes[first].val, nodes[second].val = nodes[second].val, nodes[first].val
        self.assertIsNone(Solution().recoverTree(root))
        self.assertEqual(tree_records(root), before)

    def test_every_pair_of_swapped_values_in_all_small_bst_shapes(self):
        trees = checks = 0
        for size in range(2, 8):
            for shape in shapes(size):
                root = bst_from_shape(shape, range(size))
                before = tree_records(root)
                nodes = inorder_nodes(root)
                for first, second in combinations(range(size), 2):
                    self.check_swap(root, nodes, before, first, second)
                    checks += 1
                trees += 1
        self.assertEqual((trees, checks), (624, 11510))

    def test_maximum_deep_chains_value_limits_and_adjacent_swaps(self):
        values = [-2**31] + list(range(998)) + [2**31 - 1]
        for left_chain in (False, True):
            nodes = [TreeNode(value) for value in values]
            if left_chain:
                for index in range(999, 0, -1):
                    nodes[index].left = nodes[index - 1]
                root = nodes[-1]
            else:
                for index in range(999):
                    nodes[index].right = nodes[index + 1]
                root = nodes[0]
            before = tree_records(root)
            for first, second in ((0, 999), (0, 1), (498, 499)):
                self.check_swap(root, nodes, before, first, second)


if __name__ == '__main__':
    unittest.main()
