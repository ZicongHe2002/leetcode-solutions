import unittest
from collections import deque

from python.p0232_implement_queue_using_stacks import MyQueue


def valid_queue_programs(prefix=(), values=()):
    yield prefix
    if len(prefix) == 6:
        return
    for value in (1, 2):
        yield from valid_queue_programs(prefix + (('push', value),), values + (value,))
    yield from valid_queue_programs(prefix + (('empty',),), values)
    if values:
        yield from valid_queue_programs(prefix + (('pop',),), values[1:])
        yield from valid_queue_programs(prefix + (('peek',),), values)


class StackQueueTests(unittest.TestCase):
    def test_all_valid_short_programs_against_deque(self):
        programs = 0
        for operations in valid_queue_programs():
            queue, model = MyQueue(), deque()
            for action in operations:
                if action[0] == 'push':
                    self.assertIsNone(queue.push(action[1]))
                    model.append(action[1])
                elif action[0] == 'empty':
                    result = queue.empty()
                    self.assertIs(type(result), bool)
                    self.assertEqual(result, not model)
                else:
                    result = queue.pop() if action[0] == 'pop' else queue.peek()
                    self.assertIs(type(result), int)
                    self.assertEqual(result, model.popleft() if action[0] == 'pop' else model[0])
            programs += 1
        self.assertEqual(programs, 8065)

    def test_maximum_calls_fifo_order_peek_and_empty(self):
        queue = MyQueue()
        values = [index % 9 + 1 for index in range(50)]
        for value in values:
            self.assertIsNone(queue.push(value))
        for value in values:
            self.assertEqual(queue.pop(), value)
        queue = MyQueue()
        for index in range(99):
            queue.push(index % 9 + 1)
        self.assertEqual(queue.peek(), 1)
        queue = MyQueue()
        for _ in range(100):
            self.assertTrue(queue.empty())


if __name__ == '__main__':
    unittest.main()
