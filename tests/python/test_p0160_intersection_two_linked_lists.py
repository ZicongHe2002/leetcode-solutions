import unittest
from itertools import product

from python.p0160_intersection_two_linked_lists import ListNode, Solution


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


class IntersectionTests(unittest.TestCase):
    def check(self, a_values, b_values, common_values):
        a_nodes = build_nodes(a_values)
        b_nodes = build_nodes(b_values)
        common = build_nodes(common_values)
        common_head = common[0] if common else None
        if a_nodes:
            a_nodes[-1].next = common_head
        if b_nodes:
            b_nodes[-1].next = common_head
        a_path, b_path = a_nodes + common, b_nodes + common
        head_a = a_path[0] if a_path else None
        head_b = b_path[0] if b_path else None
        a_ids = {id(node) for node in a_path}
        expected = next((node for node in b_path if id(node) in a_ids), None)
        self.assertIs(Solution().getIntersectionNode(head_a, head_b), expected)
        assert_path(self, head_a, a_path)
        assert_path(self, head_b, b_path)
        self.assertEqual([node.val for node in a_nodes + b_nodes + common],
                         list(a_values) + list(b_values) + list(common_values))

    def test_all_small_shared_tail_graphs_and_empty_extensions_against_identity_sets(self):
        checks = 0
        for a_size in range(4):
            for b_size in range(4):
                for common_size in range(4):
                    for values in product((1, 2), repeat=a_size + b_size + common_size):
                        self.check(values[:a_size], values[a_size:a_size + b_size],
                                   values[a_size + b_size:])
                        checks += 1
        self.assertEqual(checks, 3375)

    def test_maximum_lists_equal_values_and_shared_node_identity(self):
        self.check([1] * 15000, [1] * 10000, [1] * 15000)
        self.check([100000] * 30000, [100000] * 30000, [])
        self.check([1] * 29999, [], [1])
        self.check([], [1], [])
        self.check([], [], [])


if __name__ == '__main__':
    unittest.main()
