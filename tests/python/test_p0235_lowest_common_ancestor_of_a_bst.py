from functools import lru_cache
from itertools import combinations
import unittest

from python.p0235_lowest_common_ancestor_of_a_bst import Solution, TreeNode



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



def parent_pointer_lca(root, first, second):
    parents, pending = {root: None}, [root]
    while pending:
        node = pending.pop()
        for child in (node.left, node.right):
            if child is not None:
                parents[child] = node
                pending.append(child)
    ancestors = set()
    while first is not None:
        ancestors.add(first)
        first = parents[first]
    while second not in ancestors:
        second = parents[second]
    return second


class BSTAncestorIdentityTests(unittest.TestCase):
    def test_all_small_shapes_and_distinct_target_pairs_both_orders(self):
        trees = checks = 0
        for size in range(2, 8):
            for shape in shapes(size):
                root = bst_from_shape(shape, range(size))
                nodes = inorder_nodes(root)
                before = tree_records(root)
                for first, second in combinations(nodes, 2):
                    expected = parent_pointer_lca(root, first, second)
                    for p, q in ((first, second), (second, first)):
                        self.assertIs(Solution().lowestCommonAncestor(root, p, q), expected)
                        self.assertEqual(tree_records(root), before)
                        checks += 1
                trees += 1
        self.assertEqual((trees, checks), (624, 23020))

    def test_maximum_node_count_height_and_value_limits(self):
        values = [-10**9] + list(range(99998)) + [10**9]
        for left_chain in (False, True):
            nodes = [TreeNode(value) for value in values]
            if left_chain:
                for index in range(99999, 0, -1):
                    nodes[index].left = nodes[index - 1]
                root = nodes[-1]
            else:
                for index in range(99999):
                    nodes[index].right = nodes[index + 1]
                root = nodes[0]
            before = tree_records(root)
            for first, second in ((0, 99999), (99998, 99999), (123, 54321)):
                expected = nodes[max(first, second) if left_chain else min(first, second)]
                for p, q in ((nodes[first], nodes[second]), (nodes[second], nodes[first])):
                    self.assertIs(Solution().lowestCommonAncestor(root, p, q), expected)
            self.assertEqual(tree_records(root), before)


if __name__ == '__main__':
    unittest.main()
