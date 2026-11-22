import unittest
from itertools import product

from python.p0328_odd_even_linked_list import ListNode, Solution


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


class OddEvenListTests(unittest.TestCase):
    def check(self, values):
        nodes = build_nodes(values)
        head = nodes[0] if nodes else None
        expected = nodes[::2] + nodes[1::2]
        result = Solution().oddEvenList(head)
        self.assertIs(result, head)
        assert_path(self, result, expected)
        self.assertEqual([node.val for node in nodes], list(values))

    def test_all_small_lists_against_position_partition(self):
        checks = 0
        for size in range(9):
            for values in product(range(-1, 2), repeat=size):
                self.check(values)
                checks += 1
        self.assertEqual(checks, 9841)

    def test_parity_lengths_equal_values_and_maximum_contract(self):
        values = [-1000000 if index % 2 else 1000000 for index in range(10000)]
        self.check(values)
        self.check(values[:-1])
        self.check([0] * 10000)
        self.check([2, 1, 3, 5, 6, 4, 7])
        self.check([])


if __name__ == '__main__':
    unittest.main()
