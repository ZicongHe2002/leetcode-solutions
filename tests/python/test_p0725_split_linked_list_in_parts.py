import unittest
from functools import lru_cache
from itertools import product

from python.p0725_split_linked_list_in_parts import Solution


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


@lru_cache(None)
def unique_balanced_partition(total, parts):
    candidates = [sizes for sizes in weak_compositions(total, parts)
                  if all(a >= b for a, b in zip(sizes, sizes[1:])) and max(sizes) - min(sizes) <= 1]
    assert len(candidates) == 1
    return candidates[0]


class SplitListPartsTests(unittest.TestCase):
    def check(self, values, k, expected_sizes=None):
        nodes = [ListNode(value) for value in values]
        for left, right in zip(nodes, nodes[1:]):
            left.next = right
        parts = Solution().splitListToParts(nodes[0] if nodes else None, k)
        self.assertIs(type(parts), list)
        self.assertEqual(len(parts), k)
        actual_sizes, seen, flattened = [], set(), []
        for head in parts:
            size, node = 0, head
            while node is not None:
                self.assertNotIn(id(node), seen)
                seen.add(id(node))
                flattened.append(node)
                size += 1
                node = node.next
            actual_sizes.append(size)
        self.assertEqual([id(node) for node in flattened], [id(node) for node in nodes])
        self.assertEqual([node.val for node in flattened], values)
        expected = unique_balanced_partition(len(values), k) if expected_sizes is None else expected_sizes
        self.assertEqual(actual_sizes, list(expected))

    def test_all_small_binary_lists_and_part_counts_against_composition_search(self):
        checked = 0
        for size in range(8):
            for values in product((0, 1000), repeat=size):
                for k in range(1, 7):
                    self.check(list(values), k)
                    checked += 1
        self.assertEqual(checked, 1530)

    def test_thousand_nodes_empty_lists_and_exact_uneven_boundaries(self):
        self.check([1000] * 1000, 1, [1000])
        self.check(list(range(1000)), 7, [143] * 6 + [142])
        self.check([0] * 1000, 50, [20] * 50)
        self.check([], 50, [0] * 50)
        self.check([1, 2, 3], 5, [1, 1, 1, 0, 0])
        self.check(list(range(1, 11)), 3, [4, 3, 3])


if __name__ == '__main__':
    unittest.main()
