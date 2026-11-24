import unittest
from itertools import product

from python.p0203_remove_linked_list_elements import ListNode, Solution


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


class RemoveElementTests(unittest.TestCase):
    def check(self, values, val):
        nodes = build_nodes(values)
        expected = [node for node in nodes if node.val != val]
        result = Solution().removeElements(nodes[0] if nodes else None, val)
        assert_path(self, result, expected)
        self.assertEqual([node.val for node in nodes], list(values))

    def test_all_small_lists_and_targets_against_node_filter(self):
        arrays = checks = 0
        for size in range(8):
            for values in product((1, 2, 3), repeat=size):
                arrays += 1
                for val in range(5):
                    self.check(values, val)
                    checks += 1
        self.assertEqual((arrays, checks), (3280, 16400))

    def test_consecutive_runs_empty_and_maximum_contract(self):
        self.check([50] * 10000, 50)
        self.check([1, 50] * 5000, 50)
        self.check([50] * 10000, 0)
        self.check([1, 1, 2, 3, 1, 1], 1)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
