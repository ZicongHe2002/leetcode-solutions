from itertools import product
import unittest

from python.p0025_reverse_nodes_in_k_group import ListNode, Solution



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



class ReverseCompleteGroupsTests(unittest.TestCase):
    def check(self, values, size):
        head, nodes = linked(values)
        expected = []
        for start in range(0, len(nodes), size):
            group = nodes[start:start + size]
            expected.extend(reversed(group) if len(group) == size else group)
        result = Solution().reverseKGroup(head, size)
        assert_nodes(self, result, expected)
        self.assertEqual([node.val for node in nodes], values)

    def test_all_small_binary_lists_and_legal_group_sizes(self):
        arrays = checks = 0
        for length in range(1, 8):
            for values in product((0, 1), repeat=length):
                arrays += 1
                for size in range(1, length + 1):
                    self.check(list(values), size)
                    checks += 1
        self.assertEqual((arrays, checks), (254, 1538))

    def test_maximum_length_complete_and_incomplete_tail_groups(self):
        values = [index % 1001 for index in range(5000)]
        for size in (1, 2, 3, 2499, 2500, 4999, 5000):
            self.check(values, size)
        self.check([1, 2, 3, 4, 5], 2)
        self.check([1, 2, 3, 4, 5], 3)


if __name__ == '__main__':
    unittest.main()
