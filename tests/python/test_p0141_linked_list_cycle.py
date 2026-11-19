import unittest

from python.p0141_linked_list_cycle import ListNode, Solution


def visited_identity_oracle(head):
    visited = set()
    while head is not None:
        identity = id(head)
        if identity in visited:
            return True
        visited.add(identity)
        head = head.next
    return False


class LinkedListCycleTests(unittest.TestCase):
    def test_all_small_cycle_entries_and_unchanged_structure(self):
        solution = Solution()
        for length in range(9):
            for entry in range(-1, length):
                with self.subTest(length=length, entry=entry):
                    nodes = [ListNode(7) for _ in range(length)]
                    for left, right in zip(nodes, nodes[1:]):
                        left.next = right
                    if entry >= 0:
                        nodes[-1].next = nodes[entry]
                    head = nodes[0] if nodes else None
                    before = [node.next for node in nodes]
                    expected = visited_identity_oracle(head)
                    self.assertEqual(expected, entry >= 0)
                    self.assertEqual(solution.hasCycle(head), expected)
                    for node, successor in zip(nodes, before):
                        self.assertIs(node.next, successor)
                        self.assertEqual(node.val, 7)


if __name__ == "__main__":
    unittest.main()
