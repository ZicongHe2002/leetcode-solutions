import unittest
from itertools import product

from python.p0092_reverse_linked_list_ii import ListNode, Solution


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


class ReverseBetweenTests(unittest.TestCase):
    def check(self, values, left, right):
        nodes = build_nodes(values)
        expected = nodes[:left - 1] + nodes[left - 1:right][::-1] + nodes[right:]
        result = Solution().reverseBetween(nodes[0], left, right)
        assert_path(self, result, expected)
        self.assertEqual([node.val for node in nodes], list(values))

    def test_all_small_lists_and_intervals_against_node_slice(self):
        arrays = checks = 0
        for size in range(1, 7):
            for values in product(range(-1, 2), repeat=size):
                arrays += 1
                for left in range(1, size + 1):
                    for right in range(left, size + 1):
                        self.check(values, left, right)
                        checks += 1
        self.assertEqual((arrays, checks), (1092, 19956))

    def test_head_tail_full_and_maximum_contract(self):
        values = [index - 250 for index in range(500)]
        for left, right in [(1, 500), (1, 2), (499, 500), (2, 499), (250, 250)]:
            self.check(values, left, right)
        self.check([500] * 500, 1, 500)
        self.check([-500], 1, 1)


if __name__ == '__main__':
    unittest.main()
