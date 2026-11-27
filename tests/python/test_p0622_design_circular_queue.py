from itertools import product
import unittest

from python.p0622_design_circular_queue import MyCircularQueue


class CircularQueueListModelTests(unittest.TestCase):
    def apply(self, instance, reference, capacity, command):
        name, arguments = command
        if name == 'enQueue':
            expected = len(reference) < capacity
            if expected:
                reference.append(arguments[0])
        elif name == 'deQueue':
            expected = bool(reference)
            if expected:
                reference.pop(0)
        elif name == 'Front':
            expected = reference[0] if reference else -1
        elif name == 'Rear':
            expected = reference[-1] if reference else -1
        elif name == 'isEmpty':
            expected = not reference
        else:
            expected = len(reference) == capacity
        result = getattr(instance, name)(*arguments)
        self.assertIs(type(result), int if name in ('Front', 'Rear') else bool)
        self.assertEqual(result, expected)

    def observe(self, instance, reference, capacity):
        for name in ('Front', 'Rear', 'isEmpty', 'isFull'):
            self.apply(instance, reference, capacity, (name, ()))

    def test_all_small_capacity_short_mutation_sequences(self):
        operations = (('enQueue', (0,)), ('enQueue', (1,)), ('deQueue', ()))
        sequences = 0
        for capacity in (1, 2, 3):
            for length in range(7):
                for commands in product(operations, repeat=length):
                    instance, reference = MyCircularQueue(capacity), []
                    self.observe(instance, reference, capacity)
                    for command in commands:
                        self.apply(instance, reference, capacity, command)
                        self.observe(instance, reference, capacity)
                    sequences += 1
        self.assertEqual(sequences, 3279)

    def test_maximum_capacity_and_exact_external_call_budget_with_wraparound(self):
        capacity = 1000
        commands = [('enQueue', (value,)) for value in range(1000)]
        commands += [('enQueue', (1000,))]
        commands += [(name, ()) for name in ('Front', 'Rear', 'isEmpty', 'isFull')]
        commands += [('deQueue', ())] * 500
        commands += [('enQueue', ((value + 1000) % 1001,)) for value in range(500)]
        commands += [(name, ()) for name in ('Front', 'Rear', 'isEmpty', 'isFull')]
        for value in range(330):
            commands += [('deQueue', ()), ('enQueue', (value,)), ('Rear', ())]
        commands += [('Front', ())]
        self.assertEqual(len(commands), 3000)
        instance, reference = MyCircularQueue(capacity), []
        for command in commands:
            self.apply(instance, reference, capacity, command)


if __name__ == '__main__':
    unittest.main()
