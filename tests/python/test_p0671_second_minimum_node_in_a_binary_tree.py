import random
import unittest
from functools import lru_cache
from itertools import product

from python.p0671_second_minimum_node_in_a_binary_tree import Solution


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(leaves):
    if leaves == 1:
        return (None,)
    return tuple((left, right) for count in range(1, leaves)
                 for left in shapes(count) for right in shapes(leaves - count))


def build(shape, values):
    if shape is None:
        return Node(next(values))
    left, right = build(shape[0], values), build(shape[1], values)
    return Node(min(left.val, right.val), left, right)


def random_shape(leaves, rng):
    if leaves == 1:
        return None
    count = rng.randrange(1, leaves)
    return random_shape(count, rng), random_shape(leaves - count, rng)


def all_nodes(root):
    result, pending = [], [root]
    while pending:
        node = pending.pop()
        result.append(node)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return result


class SecondMinimumTreeTests(unittest.TestCase):
    def check(self, root, expected=None):
        original = all_nodes(root)
        before = [(node, node.val, node.left, node.right) for node in original]
        values = sorted({node.val for node in original})
        if expected is None:
            expected = values[1] if len(values) > 1 else -1
        result = Solution().findSecondMinimumValue(root)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        for node, value, left, right in before:
            self.assertEqual(node.val, value)
            self.assertIs(node.left, left)
            self.assertIs(node.right, right)

    def test_all_small_full_shapes_and_leaf_labels_against_sorted_value_set(self):
        checked = 0
        for leaves in range(1, 6):
            for shape in shapes(leaves):
                for values in product((1, 2, 5), repeat=leaves):
                    self.check(build(shape, iter(values)))
                    checked += 1
        self.assertEqual(checked, 3873)

    def test_maximum_nodes_seeded_shapes_equal_values_and_largest_candidate(self):
        rng = random.Random(671)
        for _ in range(200):
            leaves = rng.randrange(1, 14)
            values = [rng.choice((1, 2, 5, 2**31 - 1)) for _ in range(leaves)]
            self.check(build(random_shape(leaves, rng), iter(values)))
        comb = Node(2**31 - 1)
        for _ in range(12):
            comb = Node(1, Node(1), comb)
        self.assertEqual(len(all_nodes(comb)), 25)
        self.check(comb, 2**31 - 1)
        self.check(build(random_shape(13, rng), iter([7] * 13)), -1)
        self.check(Node(2**31 - 1), -1)
        self.check(Node(2, Node(2), Node(5, Node(5), Node(7))), 5)


if __name__ == '__main__':
    unittest.main()
