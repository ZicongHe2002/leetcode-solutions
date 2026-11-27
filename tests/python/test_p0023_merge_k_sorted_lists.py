from itertools import combinations_with_replacement, product
import unittest

from python.p0023_merge_k_sorted_lists import ListNode, Solution



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



class MergeKLinkedListsTests(unittest.TestCase):
    def check(self, arrays):
        pairs = [linked(values) for values in arrays]
        heads = [head for head, _ in pairs]
        before_heads = heads[:]
        all_nodes = [node for _, nodes in pairs for node in nodes]
        before_values = [node.val for node in all_nodes]
        expected = sorted(all_nodes, key=lambda node: node.val)
        result = Solution().mergeKLists(heads)
        assert_nodes(self, result, expected)
        self.assertEqual(heads, before_heads)
        self.assertEqual([node.val for node in all_nodes], before_values)

    def test_all_small_sorted_list_groups_against_stable_sort(self):
        arrays = [values for size in range(4)
                  for values in combinations_with_replacement((-1, 0, 1), size)]
        checks = 0
        for count in range(4):
            for group in product(arrays, repeat=count):
                self.check(group)
                checks += 1
        self.assertEqual((len(arrays), checks), (20, 8421))

    def test_maximum_k_total_length_duplicates_and_empty_lists(self):
        self.check([[value] for value in range(4999, -5001, -1)])
        self.check([list(range(-250, 250)) for _ in range(20)])
        self.check([[] for _ in range(10000)])
        self.check([[-10000, 10000], [], [-10000, 10000]])


if __name__ == '__main__':
    unittest.main()
