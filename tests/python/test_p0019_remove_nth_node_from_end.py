import unittest
from itertools import product

from python.p0019_remove_nth_node_from_end import ListNode, Solution


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


class RemoveNthTests(unittest.TestCase):
    def check(self, values, n):
        nodes = build_nodes(values)
        expected = [node for index, node in enumerate(nodes) if index != len(nodes) - n]
        result = Solution().removeNthFromEnd(nodes[0], n)
        assert_path(self, result, expected)
        self.assertEqual([node.val for node in nodes], list(values))

    def test_all_small_lists_and_valid_offsets_against_node_index_oracle(self):
        arrays = checks = 0
        for size in range(1, 8):
            for values in product(range(3), repeat=size):
                arrays += 1
                for n in range(1, size + 1):
                    self.check(values, n)
                    checks += 1
        self.assertEqual((arrays, checks), (3279, 21324))

    def test_head_tail_singleton_and_maximum_contract(self):
        for n in range(1, 31):
            self.check([100] * 30, n)
        self.check([0], 1)
        self.check([1, 2, 3, 4, 5], 2)
        self.check([1, 2], 1)
        self.check([1, 2], 2)


if __name__ == '__main__':
    unittest.main()
