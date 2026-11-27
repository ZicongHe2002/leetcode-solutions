import unittest

from python.p0155_min_stack import MinStack


def valid_programs(prefix=(), values=()):
    yield prefix
    if len(prefix) == 6:
        return
    for value in (-2**31, 0, 2**31 - 1):
        yield from valid_programs(prefix + (('push', value),), values + (value,))
    if values:
        yield from valid_programs(prefix + (('pop',),), values[:-1])
        for action in ('top', 'getMin'):
            yield from valid_programs(prefix + ((action,),), values)


class MinimumStackTests(unittest.TestCase):
    def test_all_valid_short_programs_against_plain_list_minimum(self):
        programs = 0
        for operations in valid_programs():
            stack, model = MinStack(), []
            for action in operations:
                if action[0] == 'push':
                    self.assertIsNone(stack.push(action[1]))
                    model.append(action[1])
                elif action[0] == 'pop':
                    self.assertIsNone(stack.pop())
                    model.pop()
                else:
                    result = stack.top() if action[0] == 'top' else stack.getMin()
                    self.assertIs(type(result), int)
                    self.assertEqual(result, model[-1] if action[0] == 'top' else min(model))
            programs += 1
        self.assertEqual(programs, 23917)

    def test_maximum_call_count_integer_endpoints_and_restored_prefix(self):
        stack = MinStack()
        values = (-2**31, 2**31 - 1, 0)
        for index in range(15000):
            self.assertIsNone(stack.push(values[index % 3]))
        for _ in range(14998):
            self.assertIsNone(stack.pop())
        self.assertEqual(stack.getMin(), -2**31)
        self.assertEqual(stack.top(), 2**31 - 1)


if __name__ == '__main__':
    unittest.main()
