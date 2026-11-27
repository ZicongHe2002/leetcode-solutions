import unittest

from python.p0002_add_two_numbers import ListNode, Solution


def linked_number(number):
    nodes = [ListNode(int(digit)) for digit in reversed(str(number))]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return nodes[0], nodes


class LinkedAdditionTests(unittest.TestCase):
    def check(self, first, second):
        head1, nodes1 = linked_number(first)
        head2, nodes2 = linked_number(second)
        inputs = nodes1 + nodes2
        before = [(node.val, node.next) for node in inputs]
        expected = [int(digit) for digit in reversed(str(first + second))]
        current = Solution().addTwoNumbers(head1, head2)
        seen = set()
        for digit in expected:
            self.assertIsInstance(current, ListNode)
            self.assertNotIn(current, inputs)
            self.assertNotIn(current, seen)
            self.assertIs(type(current.val), int)
            self.assertEqual(current.val, digit)
            seen.add(current)
            current = current.next
        self.assertIsNone(current)
        self.assertEqual([(node.val, node.next) for node in inputs], before)

    def test_all_two_digit_numbers_against_integer_sum(self):
        checks = 0
        for first in range(100):
            for second in range(100):
                self.check(first, second)
                checks += 1
        self.assertEqual(checks, 10000)

    def test_maximum_input_length_carry_chain_and_zero(self):
        largest = int('9' * 100)
        self.check(largest, largest)
        self.check(largest, 1)
        self.check(10**99, 0)
        self.check(0, 0)
        self.check(342, 465)
        self.check(9999999, 9999)


if __name__ == '__main__':
    unittest.main()
