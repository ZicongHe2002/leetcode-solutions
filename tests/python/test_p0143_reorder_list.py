from itertools import product
import unittest

from python.p0143_reorder_list import ListNode, Solution



def linked(values):
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return nodes[0] if nodes else None, nodes


def assert_nodes(test, result, expected):
    for node in expected:
        test.assertIs(result, node)
        result = result.next
    test.assertIsNone(result)



class FoldedReorderTests(unittest.TestCase):
    def check(self, values):
        head, nodes = linked(values)
        expected = []
        for left in range((len(nodes) + 1) // 2):
            expected.append(nodes[left])
            right = len(nodes) - 1 - left
            if right != left:
                expected.append(nodes[right])
        result = Solution().reorderList(head)
        self.assertIsNone(result)
        assert_nodes(self, head, expected)
        self.assertEqual([node.val for node in nodes], values)

    def test_all_small_nonempty_lists_against_alternating_indices(self):
        checks = 0
        for length in range(1, 9):
            for values in product((1, 2), repeat=length):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 510)

    def test_maximum_length_odd_even_and_single_node(self):
        for length in (50000, 49999):
            self.check([index % 1000 + 1 for index in range(length)])
        self.check([1000])
        self.check([1, 1000])
        self.check([1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
