from itertools import product
import unittest

from python.p0707_design_linked_list import MyLinkedList


class LinkedListArrayOracleTests(unittest.TestCase):
    def apply(self, instance, reference, command):
        name, arguments = command
        expected = None
        if name == 'get':
            index = arguments[0]
            expected = reference[index] if index < len(reference) else -1
        elif name == 'addAtHead':
            reference.insert(0, arguments[0])
        elif name == 'addAtTail':
            reference.append(arguments[0])
        elif name == 'addAtIndex':
            index, value = arguments
            if index <= len(reference):
                reference.insert(index, value)
        elif arguments[0] < len(reference):
            reference.pop(arguments[0])
        result = getattr(instance, name)(*arguments)
        self.assertIs(type(result), int if name == 'get' else type(None))
        self.assertEqual(result, expected)

    def observe(self, instance, reference):
        for index in list(range(len(reference) + 2)) + [1000]:
            self.apply(instance, reference, ('get', (index,)))

    def test_all_short_mutation_sequences_and_empty_tail_recovery(self):
        operations = (
            ('addAtHead', (0,)), ('addAtHead', (1000,)), ('addAtTail', (1,)),
            ('addAtIndex', (0, 1)), ('addAtIndex', (1, 0)), ('addAtIndex', (4, 1000)),
            ('deleteAtIndex', (0,)), ('deleteAtIndex', (1,)), ('deleteAtIndex', (4,)),
        )
        sequences = 0
        for length in range(5):
            for commands in product(operations, repeat=length):
                instance, reference = MyLinkedList(), []
                self.observe(instance, reference)
                for command in commands:
                    self.apply(instance, reference, command)
                    self.observe(instance, reference)
                sequences += 1
        self.assertEqual(sequences, 7381)

    def test_exact_2000_calls_and_largest_valid_index(self):
        instance, reference = MyLinkedList(), []
        commands = [('addAtTail', (index,)) for index in range(1000)]
        commands += [('get', (index,)) for index in range(1000)]
        self.assertEqual(len(commands), 2000)
        for command in commands:
            self.apply(instance, reference, command)
        instance, reference = MyLinkedList(), []
        for index in range(1001):
            self.apply(instance, reference, ('addAtTail', (index,)))
        for command in (('get', (1000,)), ('deleteAtIndex', (1000,)), ('get', (1000,)),
                        ('addAtIndex', (1000, 1000)), ('get', (1000,))):
            self.apply(instance, reference, command)


if __name__ == '__main__':
    unittest.main()
