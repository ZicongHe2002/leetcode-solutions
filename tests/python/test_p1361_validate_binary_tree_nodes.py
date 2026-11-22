from itertools import product
import unittest

from python.p1361_validate_binary_tree_nodes import Solution


def try_every_root_and_expand(n, left, right):
    for root in range(n):
        seen, pending = set(), [root]
        while pending:
            node = pending.pop()
            if node in seen:
                break
            seen.add(node)
            pending.extend(child for child in (left[node], right[node]) if child != -1)
        else:
            if len(seen) == n:
                return True
    return False


class BinaryTreeEveryRootOracleTests(unittest.TestCase):
    def check(self, n, left, right, expected=None):
        before = (left[:], right[:])
        if expected is None:
            expected = try_every_root_and_expand(n, left, right)
        result = Solution().validateBinaryTreeNodes(n, left, right)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual((left, right), before)

    def test_all_small_child_slot_arrays_against_every_possible_root(self):
        checked = 0
        for n in range(1, 5):
            for children in product(range(-1, n), repeat=2 * n):
                self.check(n, list(children[:n]), list(children[n:]))
                checked += 1
        self.assertEqual(checked, 394806)

    def test_maximum_nodes_deep_tree_shared_child_and_disconnected_cycle(self):
        n = 10000
        left, right = list(range(1, n)) + [-1], [-1] * n
        self.check(n, left, right, True)
        cycle = left[:]
        cycle[-1] = 0
        self.check(n, cycle, right, False)
        duplicate = right[:]
        duplicate[0] = 1
        self.check(n, left, duplicate, False)
        disconnected = [-1] + list(range(2, n)) + [1]
        self.check(n, disconnected, right, False)
        left = [2 * node + 1 if 2 * node + 1 < n else -1 for node in range(n)]
        right = [2 * node + 2 if 2 * node + 2 < n else -1 for node in range(n)]
        self.check(n, left, right, True)


if __name__ == '__main__':
    unittest.main()
