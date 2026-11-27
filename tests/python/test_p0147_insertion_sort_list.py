from itertools import product
import unittest

from python.p0147_insertion_sort_list import ListNode, Solution



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



class LinkedInsertionSortTests(unittest.TestCase):
    def check(self, values):
        head, nodes = linked(values)
        expected = sorted(nodes, key=lambda node: node.val)
        result = Solution().insertionSortList(head)
        assert_nodes(self, result, expected)
        self.assertEqual([node.val for node in nodes], values)

    def test_all_small_nonempty_lists_against_stable_sort(self):
        checks = 0
        for length in range(1, 8):
            for values in product((-1, 0, 1), repeat=length):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_length_orderings_duplicate_stability_and_extremes(self):
        self.check(list(range(-2500, 2500)))
        self.check(list(range(2499, -2501, -1)))
        self.check([-5000, 5000, 0, -5000, 5000, 0])
        self.check([1, 1, 1, 1])
        self.check([5000])


if __name__ == '__main__':
    unittest.main()
