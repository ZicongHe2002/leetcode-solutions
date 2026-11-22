import unittest
from itertools import product

from python.p0024_swap_nodes_in_pairs import ListNode, Solution


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


class SwapPairTests(unittest.TestCase):
    def check(self, values):
        nodes = build_nodes(values)
        expected = []
        for start in range(0, len(nodes), 2):
            expected.extend(nodes[start:start + 2][::-1])
        result = Solution().swapPairs(nodes[0] if nodes else None)
        assert_path(self, result, expected)
        self.assertEqual([node.val for node in nodes], list(values))

    def test_all_small_lists_against_pairwise_node_index_permutation(self):
        checks = 0
        for size in range(8):
            for values in product(range(3), repeat=size):
                self.check(values)
                checks += 1
        self.assertEqual(checks, 3280)

    def test_odd_tail_singleton_empty_and_maximum_contract(self):
        self.check(list(range(100)))
        self.check([100] * 100)
        self.check([1, 2, 3, 4, 5])
        self.check([0])
        self.check([])


if __name__ == '__main__':
    unittest.main()
