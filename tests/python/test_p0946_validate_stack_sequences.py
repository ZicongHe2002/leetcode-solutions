from itertools import permutations
import unittest

from python.p0946_validate_stack_sequences import Solution


def outputs_of_all_interleavings(pushed):
    outputs = set()

    def visit(index, stack, popped):
        if index == len(pushed) and not stack:
            outputs.add(popped)
            return
        if index < len(pushed):
            visit(index + 1, stack + (pushed[index],), popped)
        if stack:
            visit(index, stack[:-1], popped + (stack[-1],))

    visit(0, (), ())
    return outputs


class StackSequenceInterleavingTests(unittest.TestCase):
    def check(self, pushed, popped, expected):
        before = (pushed[:], popped[:])
        result = Solution().validateStackSequences(pushed, popped)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual((pushed, popped), before)

    def test_all_small_permutations_against_all_legal_operation_interleavings(self):
        checks = 0
        for size in range(1, 8):
            pushed = list(range(size))
            legal = outputs_of_all_interleavings(pushed)
            for popped in permutations(pushed):
                self.check(pushed, list(popped), popped in legal)
                checks += 1
        self.assertEqual(checks, 5913)

    def test_maximum_length_boundaries_and_unsorted_push_order(self):
        pushed = list(range(1, 1001))
        self.check(pushed, pushed[:], True)
        self.check(pushed, pushed[::-1], True)
        self.check(pushed, [999, 1000] + list(range(1, 999)), False)
        self.check([3, 0, 1000, 2], [0, 2, 1000, 3], True)
        self.check([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False)


if __name__ == '__main__':
    unittest.main()
