import unittest
from itertools import combinations

from python.p0108_convert_sorted_array_to_bst import Solution


class SortedArrayTreeTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        root = Solution().sortedArrayToBST(values)
        self.assertEqual(values, before)
        seen = set()
        heights = {id(None): 0}
        pending = [(root, False)] if root is not None else []
        while pending:
            node, expanded = pending.pop()
            if expanded:
                left = heights[id(node.left)]
                right = heights[id(node.right)]
                self.assertLessEqual(abs(left - right), 1)
                heights[id(node)] = 1 + max(left, right)
            else:
                self.assertNotIn(id(node), seen)
                seen.add(id(node))
                pending.append((node, True))
                if node.right is not None:
                    pending.append((node.right, False))
                if node.left is not None:
                    pending.append((node.left, False))
        self.assertEqual(len(seen), len(before))
        actual, ancestors, node = [], [], root
        while ancestors or node is not None:
            while node is not None:
                ancestors.append(node)
                node = node.left
            node = ancestors.pop()
            self.assertIs(type(node.val), int)
            actual.append(node.val)
            node = node.right
        self.assertEqual(actual, before)

    def test_all_small_sorted_subsets_without_fixing_a_shape(self):
        checks = 0
        for size in range(1, 8):
            for values in combinations(range(-3, 4), size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 127)

    def test_maximum_length_extreme_values_and_empty_extension(self):
        self.check(list(range(-5000, 5000)))
        self.check([-10000, -9999, 0, 9999, 10000])
        self.check([-10000])
        self.check([-10000, 10000])
        self.check([])


if __name__ == '__main__':
    unittest.main()
