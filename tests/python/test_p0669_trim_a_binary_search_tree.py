import unittest
from functools import lru_cache
from itertools import combinations

from python.p0669_trim_a_binary_search_tree import Solution


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(values):
    if not values:
        return (None,)
    return tuple((value, left, right)
                 for i, value in enumerate(values)
                 for left in shapes(values[:i])
                 for right in shapes(values[i + 1:]))


def build(shape):
    return None if shape is None else Node(shape[0], build(shape[1]), build(shape[2]))


def trimmed_tuple(node, low, high):
    if node is None:
        return None
    if node.val < low:
        return trimmed_tuple(node.right, low, high)
    if node.val > high:
        return trimmed_tuple(node.left, low, high)
    return (node.val, trimmed_tuple(node.left, low, high),
            trimmed_tuple(node.right, low, high))


def structure(node):
    return None if node is None else (node.val, structure(node.left), structure(node.right))


def nodes(root):
    result, pending = [], [root] if root is not None else []
    seen = set()
    while pending:
        node = pending.pop()
        if id(node) in seen:
            raise AssertionError('cycle or repeated node in returned tree')
        seen.add(id(node))
        result.append(node)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return result


class TrimBSTTests(unittest.TestCase):
    def test_all_small_bsts_and_closed_intervals_against_structure_oracle(self):
        trees = checks = 0
        for size in range(1, 6):
            for values in combinations((0, 1, 3, 5, 8), size):
                for shape in shapes(values):
                    trees += 1
                    for low in range(10):
                        for high in range(low, 10):
                            root = build(shape)
                            original = nodes(root)
                            before = [(node, node.val) for node in original]
                            expected = trimmed_tuple(root, low, high)
                            result = Solution().trimBST(root, low, high)
                            retained = nodes(result)
                            self.assertEqual(structure(result), expected)
                            self.assertEqual({id(node) for node in retained},
                                             {id(node) for node in original if low <= node.val <= high})
                            self.assertTrue(all(node.val == value for node, value in before))
                            checks += 1
        self.assertEqual((trees, checks), (187, 10285))

    def test_ten_thousand_node_chains_reuse_nodes_and_include_endpoints(self):
        for direction in ('left', 'right'):
            for low, high in ((2500, 7500), (0, 10000), (5000, 5000), (10000, 10000)):
                original = [Node(value) for value in range(10000)]
                if direction == 'right':
                    for i in range(9999):
                        original[i].right = original[i + 1]
                    root = original[0]
                else:
                    for i in range(1, 10000):
                        original[i].left = original[i - 1]
                    root = original[-1]
                result = Solution().trimBST(root, low, high)
                wanted = [node for node in original if low <= node.val <= high]
                if direction == 'left':
                    wanted.reverse()
                self.assertEqual(nodes(result), wanted)
                for i, node in enumerate(wanted):
                    following = wanted[i + 1] if i + 1 < len(wanted) else None
                    self.assertIs(getattr(node, direction), following)
                    self.assertIsNone(getattr(node, 'right' if direction == 'left' else 'left'))
                self.assertEqual([node.val for node in original], list(range(10000)))


if __name__ == '__main__':
    unittest.main()
