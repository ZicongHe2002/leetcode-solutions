import unittest
from itertools import product

from python.p0086_partition_list import ListNode, Solution


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


class PartitionListTests(unittest.TestCase):
    def check(self, values, x):
        nodes = build_nodes(values)
        expected = [node for node in nodes if node.val < x] + [node for node in nodes if node.val >= x]
        result = Solution().partition(nodes[0] if nodes else None, x)
        assert_path(self, result, expected)
        self.assertEqual([node.val for node in nodes], list(values))

    def test_all_small_lists_and_pivots_against_stable_node_filter(self):
        arrays = checks = 0
        for size in range(8):
            for values in product(range(-1, 2), repeat=size):
                arrays += 1
                for x in range(-2, 3):
                    self.check(values, x)
                    checks += 1
        self.assertEqual((arrays, checks), (3280, 16400))

    def test_equal_boundary_and_maximum_contract(self):
        values = [100, -100] * 100
        for x in [-200, -100, 0, 100, 200]:
            self.check(values, x)
        self.check([1, 4, 3, 2, 5, 2], 3)
        self.check([0] * 200, 0)
        self.check([], 200)


if __name__ == '__main__':
    unittest.main()
