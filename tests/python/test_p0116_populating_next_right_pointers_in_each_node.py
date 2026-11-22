from collections import deque
from itertools import product
import unittest

from python.p0116_populating_next_right_pointers_in_each_node import Node, Solution



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



class PerfectNextLinkTests(unittest.TestCase):
    def test_all_small_perfect_trees_against_child_level_order(self):
        checks = 0
        for height in range(4):
            size = 2**height - 1
            for values in product((-1, 1), repeat=size):
                check_next_links(self, complete(values))
                checks += 1
        self.assertEqual(checks, 139)

    def test_maximum_perfect_tree_duplicates_and_value_limits(self):
        check_next_links(self, complete([index % 2001 - 1000 for index in range(4095)]))
        check_next_links(self, complete([7] * 31))
        check_next_links(self, complete([-1000, -1000, 1000]))
        check_next_links(self, None)


if __name__ == '__main__':
    unittest.main()
