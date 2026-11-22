from itertools import product
import unittest

from python.p0641_design_circular_deque import MyCircularDeque


class CircularDequeListModelTests(unittest.TestCase):
    def apply(self, instance, reference, capacity, command):
        name, arguments = command
        if name in ('insertFront', 'insertLast'):
            expected = len(reference) < capacity
            if expected:
                if name == 'insertFront':
                    reference.insert(0, arguments[0])
                else:
                    reference.append(arguments[0])
        elif name in ('deleteFront', 'deleteLast'):
            expected = bool(reference)
            if expected:
                reference.pop(0 if name == 'deleteFront' else -1)
        elif name == 'getFront':
            expected = reference[0] if reference else -1
        elif name == 'getRear':
            expected = reference[-1] if reference else -1
        elif name == 'isEmpty':
            expected = not reference
        else:
            expected = len(reference) == capacity
        result = getattr(instance, name)(*arguments)
        self.assertIs(type(result), int if name in ('getFront', 'getRear') else bool)
        self.assertEqual(result, expected)

    def observe(self, instance, reference, capacity):
        for name in ('getFront', 'getRear', 'isEmpty', 'isFull'):
            self.apply(instance, reference, capacity, (name, ()))

    def test_all_short_mutation_sequences_with_both_ends(self):
        operations = (('insertFront', (0,)), ('insertFront', (1,)),
                      ('insertLast', (0,)), ('insertLast', (1,)),
                      ('deleteFront', ()), ('deleteLast', ()))
        sequences = 0
        for capacity in (1, 2, 3):
            for length in range(6):
                for commands in product(operations, repeat=length):
                    instance, reference = MyCircularDeque(capacity), []
                    self.observe(instance, reference, capacity)
                    for command in commands:
                        self.apply(instance, reference, capacity, command)
                        self.observe(instance, reference, capacity)
                    sequences += 1
        self.assertEqual(sequences, 27993)

    def test_maximum_capacity_and_exact_call_budget_mixed_wraparound(self):
        capacity = 1000
        commands = [('insertLast', (value,)) for value in range(1000)]
        commands += [('insertFront', (1000,))]
        commands += [(name, ()) for name in ('getFront', 'getRear', 'isEmpty', 'isFull')]
        commands += [('deleteFront', ())] * 300
        commands += [('insertLast', (value,)) for value in range(300)]
        commands += [(name, ()) for name in ('getFront', 'getRear', 'isEmpty', 'isFull')]
        for value in range(195):
            commands += [('deleteLast', ()), ('insertFront', (700 + value,))]
        commands += [('getFront', ())]
        self.assertEqual(len(commands), 2000)
        instance, reference = MyCircularDeque(capacity), []
        for command in commands:
            self.apply(instance, reference, capacity, command)


if __name__ == '__main__':
    unittest.main()
