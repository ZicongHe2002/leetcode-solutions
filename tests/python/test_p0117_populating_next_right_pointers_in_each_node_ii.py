from collections import deque
from functools import lru_cache
from itertools import product
import unittest

from python.p0117_populating_next_right_pointers_in_each_node_ii import Node, Solution



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
        node = Node(next(values))
        node.left = build(current[0])
        node.right = build(current[1])
        return node

    return build(shape)



def levels_by_children(root):
    levels = []
    queue = deque([root]) if root is not None else deque()
    while queue:
        level = [queue.popleft() for _ in range(len(queue))]
        levels.append(level)
        for node in level:
            queue.extend(child for child in (node.left, node.right) if child is not None)
    return levels


def check_next_links(test, root):
    levels = levels_by_children(root)
    nodes = [node for level in levels for node in level]
    before = [(node.val, node.left, node.right) for node in nodes]
    test.assertTrue(all(node.next is None for node in nodes))
    test.assertIs(Solution().connect(root), root)
    for level in levels:
        for index, node in enumerate(level):
            expected = level[index + 1] if index + 1 < len(level) else None
            test.assertIs(node.next, expected)
    test.assertEqual([(node.val, node.left, node.right) for node in nodes], before)


def complete(values):
    nodes = [Node(value) for value in values]
    for index, node in enumerate(nodes):
        if 2 * index + 1 < len(nodes):
            node.left = nodes[2 * index + 1]
        if 2 * index + 2 < len(nodes):
            node.right = nodes[2 * index + 2]
    return nodes[0] if nodes else None



class SparseNextLinkTests(unittest.TestCase):
    def test_all_small_tree_shapes_and_values_against_child_levels(self):
        checks = 0
        for size in range(7):
            for shape in shapes(size):
                for values in product((-1, 1), repeat=size):
                    check_next_links(self, materialize(shape, values))
                    checks += 1
        self.assertEqual(checks, 10067)

    def test_maximum_width_and_depth_with_sparse_cross_parent_links(self):
        check_next_links(self, complete([index % 201 - 100 for index in range(6000)]))
        root = current = Node(-100)
        for index in range(1, 6000):
            child = Node(index % 201 - 100)
            if index % 2:
                current.left = child
            else:
                current.right = child
            current = child
        check_next_links(self, root)
        root = Node(0, Node(-100), Node(100))
        root.left.right = Node(1)
        root.right.right = Node(1)
        check_next_links(self, root)


if __name__ == '__main__':
    unittest.main()
