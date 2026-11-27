import random
import unittest

from python.p0716_max_stack import MaxStack


def reference_operation(values, operation, argument=None):
    if operation == 'push':
        values.append(argument)
        return None
    if operation == 'pop':
        return values.pop()
    if operation == 'top':
        return values[-1]
    if operation == 'peekMax':
        return max(values)
    maximum = max(values)
    index = max(i for i, value in enumerate(values) if value == maximum)
    return values.pop(index)


def legal_programs(prefix=(), values=(), maximum=5):
    if prefix:
        yield prefix
    if len(prefix) == maximum:
        return
    choices = [('push', value) for value in (-1, 0, 1)]
    if values:
        choices += [(operation, None) for operation in ('pop', 'top', 'peekMax', 'popMax')]
    for operation, argument in choices:
        updated = list(values)
        reference_operation(updated, operation, argument)
        yield from legal_programs(prefix + ((operation, argument),), tuple(updated), maximum)


class MaxStackTests(unittest.TestCase):
    def check(self, program):
        obj, values = MaxStack(), []
        for operation, argument in program:
            expected = reference_operation(values, operation, argument)
            result = obj.push(argument) if operation == 'push' else getattr(obj, operation)()
            if operation == 'push':
                self.assertIsNone(result)
            else:
                self.assertIs(type(result), int)
                self.assertEqual(result, expected, program)
            if values:
                self.assertEqual(obj.top(), values[-1])
                self.assertEqual(obj.peekMax(), max(values))

    def test_all_short_legal_api_programs_and_seeded_mixed_updates_against_list(self):
        for program in legal_programs():
            self.check(program)
        rng = random.Random(716)
        for _ in range(200):
            program, values = [], []
            for _ in range(200):
                operation = rng.choice(('push', 'pop', 'top', 'peekMax', 'popMax')) if values else 'push'
                argument = rng.randrange(-10, 11) if operation == 'push' else None
                reference_operation(values, operation, argument)
                program.append((operation, argument))
            self.check(program)

    def test_one_hundred_thousand_calls_and_topmost_equal_maximum(self):
        obj, calls = MaxStack(), 0
        for value in range(50000):
            obj.push(value)
            calls += 1
        for i in range(50000):
            result = obj.popMax() if i % 2 == 0 else obj.pop()
            self.assertEqual(result, 49999 - i)
            calls += 1
        self.assertEqual(calls, 100000)
        self.check((('push', 5), ('push', 1), ('push', 5), ('top', None), ('popMax', None),
                    ('top', None), ('peekMax', None), ('pop', None), ('top', None)))
        self.check((('push', -10**7), ('push', 10**7), ('push', 0), ('push', 10**7),
                    ('popMax', None), ('pop', None), ('popMax', None), ('pop', None)))


if __name__ == '__main__':
    unittest.main()
