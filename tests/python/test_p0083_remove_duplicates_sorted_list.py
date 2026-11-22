import unittest
from itertools import combinations_with_replacement

from python.p0083_remove_duplicates_sorted_list import ListNode, Solution


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


class KeepFirstDuplicateTests(unittest.TestCase):
    def check(self, values):
        nodes = build_nodes(values)
        seen = set()
        expected = []
        for node in nodes:
            if node.val not in seen:
                seen.add(node.val)
                expected.append(node)
        head = nodes[0] if nodes else None
        result = Solution().deleteDuplicates(head)
        self.assertIs(result, head)
        assert_path(self, result, expected)
        self.assertEqual([node.val for node in nodes], list(values))

    def test_all_small_sorted_lists_against_first_occurrence_identity_oracle(self):
        checks = 0
        for size in range(9):
            for values in combinations_with_replacement(range(-2, 3), size):
                self.check(values)
                checks += 1
        self.assertEqual(checks, 1287)

    def test_repeated_runs_empty_and_maximum_contract(self):
        self.check([1, 1, 2, 3, 3])
        self.check([100] * 300)
        self.check([-100] * 100 + [0] * 100 + [100] * 100)
        self.check(list(range(-100, 101)))
        self.check([])


if __name__ == '__main__':
    unittest.main()
