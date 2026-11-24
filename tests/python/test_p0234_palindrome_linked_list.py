import unittest
from itertools import product

from python.p0234_palindrome_linked_list import ListNode, Solution


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


class PalindromeListTests(unittest.TestCase):
    def check(self, values):
        nodes = build_nodes(values)
        head = nodes[0] if nodes else None
        result = Solution().isPalindrome(head)
        self.assertIs(type(result), bool)
        self.assertEqual(result, list(values) == list(values)[::-1])
        assert_path(self, head, nodes)
        self.assertEqual([node.val for node in nodes], list(values))

    def test_all_small_lists_and_empty_extension_against_value_reversal(self):
        checks = 0
        for size in range(9):
            for values in product(range(3), repeat=size):
                self.check(values)
                checks += 1
        self.assertEqual(checks, 9841)

    def test_maximum_lengths_and_restoration_after_both_results(self):
        half = [index % 10 for index in range(50000)]
        even = half + half[::-1]
        self.check(even)
        even[-1] = (even[-1] + 1) % 10
        self.check(even)
        odd = half[:-1] + [9] + half[:-1][::-1]
        self.check(odd)
        odd[49998] = (odd[49998] + 1) % 10
        self.check(odd)
        self.check([9])
        self.check([1, 2])


if __name__ == '__main__':
    unittest.main()
