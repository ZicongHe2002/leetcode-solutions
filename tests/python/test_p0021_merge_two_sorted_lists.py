from itertools import combinations_with_replacement
import unittest

from python.p0021_merge_two_sorted_lists import ListNode, Solution


def make_list(values):
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return nodes[0] if nodes else None, nodes


class MergeTwoListsTests(unittest.TestCase):
    def test_sorted_pairs_preserve_exact_nodes_and_stable_order(self):
        cases = [
            values
            for length in range(5)
            for values in combinations_with_replacement(range(-1, 2), length)
        ]
        for first in cases:
            for second in cases:
                with self.subTest(first=first, second=second):
                    head1, nodes1 = make_list(first)
                    head2, nodes2 = make_list(second)
                    expected = sorted(nodes1 + nodes2, key=lambda node: node.val)
                    result = Solution().mergeTwoLists(head1, head2)
                    for node in expected:
                        self.assertIs(result, node)
                        result = result.next
                    self.assertIsNone(result)
                    self.assertEqual([node.val for node in nodes1], list(first))
                    self.assertEqual([node.val for node in nodes2], list(second))


if __name__ == "__main__":
    unittest.main()
