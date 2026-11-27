from itertools import combinations_with_replacement
import unittest

from python.p0109_convert_sorted_list_to_binary_search_tree import ListNode, TreeNode, Solution


class SortedLinkedTreeTests(unittest.TestCase):
    def check(self, values):
        nodes = [ListNode(value) for value in values]
        for left, right in zip(nodes, nodes[1:]):
            left.next = right
        before = [(node.val, node.next) for node in nodes]
        result = Solution().sortedListToBST(nodes[0] if nodes else None)
        order, seen = [], set()

        def inspect(node):
            if node is None:
                return 0
            self.assertIsInstance(node, TreeNode)
            self.assertNotIn(node, seen)
            seen.add(node)
            left_height = inspect(node.left)
            order.append(node.val)
            right_height = inspect(node.right)
            self.assertLessEqual(abs(left_height - right_height), 1)
            return 1 + max(left_height, right_height)

        inspect(result)
        self.assertEqual(order, values)
        self.assertEqual(len(seen), len(nodes))
        self.assertEqual([(node.val, node.next) for node in nodes], before)

    def test_all_small_sorted_lists_check_inorder_and_every_balance(self):
        checks = 0
        for size in range(9):
            for values in combinations_with_replacement((-1, 0, 2), size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 165)

    def test_maximum_length_duplicates_empty_and_value_limits(self):
        values = [-100000] + list(range(-9999, 9999)) + [100000]
        self.assertEqual(len(values), 20000)
        self.check(values)
        self.check([7] * 20000)
        self.check([])
        self.check([-100000])


if __name__ == '__main__':
    unittest.main()
