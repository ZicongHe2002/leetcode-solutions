import unittest

from python.p0225_implement_stack_using_queues import MyStack


def valid_stack_programs(prefix=(), values=()):
    yield prefix
    if len(prefix) == 6:
        return
    for value in (1, 2):
        yield from valid_stack_programs(prefix + (('push', value),), values + (value,))
    yield from valid_stack_programs(prefix + (('empty',),), values)
    if values:
        yield from valid_stack_programs(prefix + (('pop',),), values[:-1])
        yield from valid_stack_programs(prefix + (('top',),), values)


class QueueStackTests(unittest.TestCase):
    def test_all_valid_short_programs_against_list_stack(self):
        programs = 0
        for operations in valid_stack_programs():
            stack, model = MyStack(), []
            for action in operations:
                if action[0] == 'push':
                    self.assertIsNone(stack.push(action[1]))
                    model.append(action[1])
                elif action[0] == 'empty':
                    result = stack.empty()
                    self.assertIs(type(result), bool)
                    self.assertEqual(result, not model)
                else:
                    result = stack.pop() if action[0] == 'pop' else stack.top()
                    self.assertIs(type(result), int)
                    self.assertEqual(result, model.pop() if action[0] == 'pop' else model[-1])
            programs += 1
        self.assertEqual(programs, 8065)

    def test_maximum_calls_lifo_order_front_peek_and_empty(self):
        stack = MyStack()
        values = [index % 9 + 1 for index in range(50)]
        for value in values:
            self.assertIsNone(stack.push(value))
        for value in reversed(values):
            self.assertEqual(stack.pop(), value)
        stack = MyStack()
        for index in range(99):
            stack.push(index % 9 + 1)
        self.assertEqual(stack.top(), 98 % 9 + 1)
        stack = MyStack()
        for _ in range(100):
            self.assertTrue(stack.empty())


if __name__ == '__main__':
    unittest.main()
