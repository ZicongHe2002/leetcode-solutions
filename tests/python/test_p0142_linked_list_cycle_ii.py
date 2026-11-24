import unittest
from itertools import product

from python.p0142_linked_list_cycle_ii import ListNode, Solution


def build_nodes(values):
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return nodes


class CycleEntryTests(unittest.TestCase):
    def check(self, values, position):
        nodes = build_nodes(values)
        if position >= 0:
            nodes[-1].next = nodes[position]
        head = nodes[0] if nodes else None
        links = [node.next for node in nodes]
        visited = set()
        expected = head
        while expected is not None and id(expected) not in visited:
            visited.add(id(expected))
            expected = expected.next
        self.assertIs(Solution().detectCycle(head), expected)
        for node, following, value in zip(nodes, links, values):
            self.assertIs(node.next, following)
            self.assertEqual(node.val, value)

    def test_all_small_node_graphs_against_identity_set_walk(self):
        arrays = checks = 0
        for size in range(7):
            for values in product(range(3), repeat=size):
                arrays += 1
                for position in range(-1, size):
                    self.check(values, position)
                    checks += 1
        self.assertEqual((arrays, checks), (1093, 7108))

    def test_maximum_lengths_and_entry_extremes_without_mutation(self):
        values = [-100000 if index % 2 else 100000 for index in range(10000)]
        for position in [-1, 0, 4321, 9999]:
            self.check(values, position)
        self.check([0], -1)
        self.check([0], 0)
        self.check([], -1)


if __name__ == '__main__':
    unittest.main()
