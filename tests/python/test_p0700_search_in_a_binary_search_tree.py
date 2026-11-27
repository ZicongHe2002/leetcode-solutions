import unittest
from functools import lru_cache
from itertools import combinations

from python.p0700_search_in_a_binary_search_tree import Solution


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(values):
    if not values:
        return (None,)
    return tuple((value, left, right) for i, value in enumerate(values)
                 for left in shapes(values[:i]) for right in shapes(values[i + 1:]))


def build(shape):
    return None if shape is None else Node(shape[0], build(shape[1]), build(shape[2]))


def all_nodes(root):
    result, pending = [], [root]
    while pending:
        node = pending.pop()
        result.append(node)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return result


class SearchBSTTests(unittest.TestCase):
    def check(self, root, target):
        nodes = all_nodes(root)
        before = [(node, node.val, node.left, node.right) for node in nodes]
        expected = next((node for node in nodes if node.val == target), None)
        self.assertIs(Solution().searchBST(root, target), expected)
        for node, value, left, right in before:
            self.assertEqual(node.val, value)
            self.assertIs(node.left, left)
            self.assertIs(node.right, right)

    def test_all_small_bsts_and_queries_against_full_node_scan(self):
        trees = checked = 0
        for size in range(1, 6):
            for values in combinations((1, 2, 4, 8, 16), size):
                for shape in shapes(values):
                    root = build(shape)
                    trees += 1
                    for target in range(1, 19):
                        self.check(root, target)
                        checked += 1
        self.assertEqual((trees, checked), (187, 3366))

    def test_five_thousand_node_chains_identity_missing_and_value_boundaries(self):
        for direction in ('left', 'right'):
            nodes = [Node(value) for value in range(1, 5001)]
            if direction == 'right':
                for i in range(4999):
                    nodes[i].right = nodes[i + 1]
                root = nodes[0]
            else:
                for i in range(1, 5000):
                    nodes[i].left = nodes[i - 1]
                root = nodes[-1]
            for target in (1, 2500, 5000, 5001, 10**7):
                self.check(root, target)
        root = Node(10**7, Node(1))
        self.check(root, 1)
        self.check(root, 10**7)


if __name__ == '__main__':
    unittest.main()
