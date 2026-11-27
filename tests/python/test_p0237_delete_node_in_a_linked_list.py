from itertools import permutations
import unittest

from python.p0237_delete_node_in_a_linked_list import Solution


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class DeleteGivenNodeTests(unittest.TestCase):
    def check(self, values, removed):
        nodes = [Node(value) for value in values]
        for first, second in zip(nodes, nodes[1:]):
            first.next = second
        expected = values[:removed] + values[removed + 1:]
        self.assertIsNone(Solution().deleteNode(nodes[removed]))
        actual = []
        seen = set()
        current = nodes[0]
        while current is not None:
            self.assertNotIn(id(current), seen)
            seen.add(id(current))
            actual.append(current.val)
            self.assertLessEqual(len(actual), len(values))
            current = current.next
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(values) - 1)

    def test_all_small_unique_lists_and_every_legal_position(self):
        cases = 0
        for size in range(2, 6):
            for values in permutations((-2, -1, 0, 1, 2), size):
                for removed in range(size - 1):
                    self.check(list(values), removed)
                    cases += 1
        self.assertEqual(cases, 980)

    def test_head_middle_penultimate_and_maximum_length(self):
        self.check([4, 5, 1, 9], 1)
        self.check([-1000, 1000], 0)
        for removed in (0, 1, 499, 998):
            self.check(list(range(1000)), removed)


if __name__ == '__main__':
    unittest.main()
