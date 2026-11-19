from itertools import product
import unittest

from python.p0206_reverse_linked_list import ListNode, Solution


class ReverseLinkedListTests(unittest.TestCase):
    def test_exact_nodes_reverse_and_restore_without_changing_values(self):
        solution = Solution()
        for length in range(7):
            for values in product(range(-1, 2), repeat=length):
                with self.subTest(values=values):
                    nodes = [ListNode(value) for value in values]
                    for left, right in zip(nodes, nodes[1:]):
                        left.next = right
                    head = nodes[0] if nodes else None
                    result = solution.reverseList(head)
                    cursor = result
                    for expected in reversed(nodes):
                        self.assertIs(cursor, expected)
                        cursor = cursor.next
                    self.assertIsNone(cursor)
                    self.assertEqual([node.val for node in nodes], list(values))
                    restored = solution.reverseList(result)
                    self.assertIs(restored, head)
                    cursor = restored
                    for expected in nodes:
                        self.assertIs(cursor, expected)
                        cursor = cursor.next
                    self.assertIsNone(cursor)


if __name__ == "__main__":
    unittest.main()
