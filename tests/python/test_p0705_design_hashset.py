from itertools import product
import unittest

from python.p0705_design_hashset import MyHashSet


class HashSetListOracleTests(unittest.TestCase):
    def apply(self, instance, reference, command):
        name, key = command
        if name == 'add':
            if key not in reference:
                reference.append(key)
            expected = None
        elif name == 'remove':
            if key in reference:
                reference.remove(key)
            expected = None
        else:
            expected = key in reference
        result = getattr(instance, name)(key)
        self.assertIs(type(result), bool if name == 'contains' else type(None))
        self.assertEqual(result, expected)

    def test_all_short_operation_sequences_against_plain_list(self):
        operations = tuple((name, key) for name in ('add', 'remove', 'contains')
                           for key in (0, 1))
        sequences = 0
        for length in range(1, 6):
            for commands in product(operations, repeat=length):
                instance, reference = MyHashSet(), []
                for command in commands:
                    self.apply(instance, reference, command)
                    for key in (0, 1, 1000000):
                        self.apply(instance, reference, ('contains', key))
                sequences += 1
        self.assertEqual(sequences, 9330)

    def test_collisions_boundary_keys_and_exact_10000_call_budget(self):
        keys = [1009 * index for index in range(992)] + [1000000]
        commands = [('add', key) for key in keys]
        names = ('contains', 'remove', 'add', 'add', 'contains', 'remove', 'add')
        while len(commands) < 9007:
            position = len(commands)
            commands.append((names[position % len(names)], keys[(position * 37) % len(keys)]))
        commands += [('contains', key) for key in keys]
        self.assertEqual(len(commands), 10000)
        self.assertEqual(len(keys), 993)
        self.assertTrue(all(0 <= key <= 1000000 for key in keys))
        instance, reference = MyHashSet(), []
        for command in commands:
            self.apply(instance, reference, command)


if __name__ == '__main__':
    unittest.main()
