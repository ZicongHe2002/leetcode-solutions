import unittest
from itertools import product

from python.p0061_rotate_list import ListNode, Solution


def build_nodes(values):
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return nodes


def assert_path(test, head, expected):
    current = head
    for node in expected:
        test.assertIs(current, node)
        current = current.next
    test.assertIsNone(current)


class RotateListTests(unittest.TestCase):
    def check(self, values, k):
        nodes = build_nodes(values)
        expected = [nodes[(index - k) % len(nodes)] for index in range(len(nodes))] if nodes else []
        result = Solution().rotateRight(nodes[0] if nodes else None, k)
        assert_path(self, result, expected)
        self.assertEqual([node.val for node in nodes], list(values))

    def test_all_small_lists_and_step_counts_against_node_coordinate_map(self):
        arrays = checks = 0
        for size in range(7):
            for values in product(range(-1, 2), repeat=size):
                arrays += 1
                for k in range(2 * size + 3):
                    self.check(values, k)
                    checks += 1
        self.assertEqual((arrays, checks), (1093, 15309))

    def test_maximum_node_count_steps_and_terminal_null(self):
        values = [(index % 201) - 100 for index in range(500)]
        for k in [0, 500, 499, 2 * 10**9, 2 * 10**9 - 1]:
            self.check(values, k)
        self.check(values[:499], 2 * 10**9)
        self.check([1, 2, 3, 4, 5], 2)
        self.check([100], 2 * 10**9)
        self.check([], 2 * 10**9)


if __name__ == '__main__':
    unittest.main()
