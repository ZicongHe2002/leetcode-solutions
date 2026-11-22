from itertools import product
import unittest

from python.p0148_sort_list import ListNode, Solution



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



class BottomUpLinkedSortTests(unittest.TestCase):
    def check(self, values):
        head, nodes = linked(values)
        expected = sorted(nodes, key=lambda node: node.val)
        result = Solution().sortList(head)
        assert_nodes(self, result, expected)
        self.assertEqual([node.val for node in nodes], values)

    def test_all_small_lists_against_stable_original_node_sort(self):
        checks = 0
        for length in range(8):
            for values in product((-1, 0, 1), repeat=length):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 3280)

    def test_maximum_length_no_recursion_and_value_boundaries(self):
        self.check(list(range(-25000, 25000)))
        self.check(list(range(24999, -25001, -1)))
        self.check([index % 1001 - 500 for index in range(50000)])
        self.check([-100000, 100000, 0, -100000, 100000])
        self.check([])


if __name__ == '__main__':
    unittest.main()
