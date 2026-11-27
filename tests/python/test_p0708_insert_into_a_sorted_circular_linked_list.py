import unittest
from collections import Counter
from itertools import combinations_with_replacement

import python.p0708_insert_into_a_sorted_circular_linked_list as implementation


class Node:
    __hash__ = None

    def __init__(self, val, next=None):
        self.val, self.next = val, next


implementation.Node = Node


def make_circle(values, rotation):
    if not values:
        return None
    nodes = [Node(value) for value in values]
    for index, node in enumerate(nodes):
        node.next = nodes[(index + 1) % len(nodes)]
    return nodes[rotation]


def cycle_nodes(head, maximum):
    result, seen, node = [], set(), head
    while node is not None and id(node) not in seen:
        if len(result) >= maximum:
            raise AssertionError('unexpected cycle length')
        seen.add(id(node))
        result.append(node)
        node = node.next
    if node is not head:
        raise AssertionError('cycle must return to supplied head')
    return result


class InsertSortedCircleTests(unittest.TestCase):
    def check(self, values, rotation, inserted):
        head = make_circle(values, rotation)
        old = cycle_nodes(head, len(values) + 1) if head is not None else []
        before = [(node, node.val, node.next) for node in old]
        result = implementation.Solution().insert(head, inserted)
        self.assertIsNotNone(result)
        if head is not None:
            self.assertIs(result, head)
        after = cycle_nodes(result, len(values) + 2)
        self.assertEqual(len(after), len(old) + 1)
        old_ids = {id(node) for node in old}
        new = [node for node in after if id(node) not in old_ids]
        self.assertEqual(len(new), 1)
        self.assertEqual(new[0].val, inserted)
        self.assertEqual([id(node) for node in after if id(node) in old_ids], [id(node) for node in old])
        self.assertEqual(Counter(node.val for node in after), Counter(values) + Counter([inserted]))
        self.assertLessEqual(sum(node.val > node.next.val for node in after), 1)
        for node, value, _ in before:
            self.assertEqual(node.val, value)
        if before:
            self.assertEqual(sum(node.next is not following for node, _, following in before), 1)
        else:
            self.assertIs(result.next, result)

    def test_all_small_multisets_heads_and_insertions_against_cycle_output_contract(self):
        checked = 0
        for size in range(7):
            for values in combinations_with_replacement((-1, 0, 1), size):
                for rotation in range(max(1, size)):
                    for inserted in range(-2, 3):
                        self.check(list(values), rotation, inserted)
                        checked += 1
        self.assertEqual(checked, 1895)

    def test_fifty_thousand_node_circles_equal_values_extrema_and_arbitrary_head(self):
        for inserted in (-10**6, 0, 10**6):
            self.check([0] * 50000, 23456, inserted)
        values = list(range(-25000, 25000))
        for inserted in (-10**6, 0, 10**6):
            self.check(values, 20000, inserted)


if __name__ == '__main__':
    unittest.main()
