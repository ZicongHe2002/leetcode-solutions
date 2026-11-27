import unittest
from itertools import product

from python.p0138_copy_list_with_random_pointer import Node, Solution


class RandomListCopyTests(unittest.TestCase):
    def check(self, values, targets):
        originals = [Node(value) for value in values]
        for index, node in enumerate(originals):
            node.next = originals[index + 1] if index + 1 < len(originals) else None
            node.random = originals[targets[index]] if targets[index] >= 0 else None
        before = [(node, node.val, node.next, node.random) for node in originals]
        original_ids = {id(node) for node in originals}
        current = Solution().copyRandomList(originals[0] if originals else None)
        copies, copied_ids = [], set()
        for value in values:
            self.assertIsNotNone(current)
            self.assertNotIn(id(current), original_ids)
            self.assertNotIn(id(current), copied_ids)
            copied_ids.add(id(current))
            self.assertEqual(current.val, value)
            copies.append(current)
            current = current.next
        self.assertIsNone(current)
        for index, copied in enumerate(copies):
            expected_next = copies[index + 1] if index + 1 < len(copies) else None
            expected_random = copies[targets[index]] if targets[index] >= 0 else None
            self.assertIs(copied.next, expected_next)
            self.assertIs(copied.random, expected_random)
        if copies:
            copies[0].val = 0 if copies[0].val != 0 else 1
            copies[0].next = None
            copies[0].random = None
        for node, value, next_node, random_node in before:
            self.assertEqual(node.val, value)
            self.assertIs(node.next, next_node)
            self.assertIs(node.random, random_node)

    def test_all_small_random_pointer_layouts(self):
        checks = 0
        for size in range(6):
            values = [index % 3 - 1 for index in range(size)]
            for targets in product(range(-1, size), repeat=size):
                self.check(values, targets)
                checks += 1
        self.assertEqual(checks, 8477)

    def test_maximum_length_repeated_values_and_random_cycles(self):
        size = 1000
        values = [10000 if index % 2 else -10000 for index in range(size)]
        for targets in ([-1] * size, [0] * size,
                        list(reversed(range(size))), list(range(size))):
            self.check(values, targets)
        self.check([7] * size, list(reversed(range(size))))
        self.check([10000], [0])


if __name__ == '__main__':
    unittest.main()
