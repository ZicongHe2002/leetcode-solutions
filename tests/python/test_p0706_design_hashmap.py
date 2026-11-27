from itertools import product
import unittest

from python.p0706_design_hashmap import MyHashMap


class HashMapPairListOracleTests(unittest.TestCase):
    def apply(self, instance, reference, command):
        name, arguments = command
        key = arguments[0]
        matches = [pair for pair in reference if pair[0] == key]
        if name == 'get':
            expected = matches[0][1] if matches else -1
        else:
            reference[:] = [pair for pair in reference if pair[0] != key]
            if name == 'put':
                reference.append((key, arguments[1]))
            expected = None
        result = getattr(instance, name)(*arguments)
        self.assertIs(type(result), int if name == 'get' else type(None))
        self.assertEqual(result, expected)

    def test_all_short_sequences_against_plain_pair_list(self):
        operations = tuple(('put', (key, value)) for key in (0, 1) for value in (0, 1))
        operations += tuple((name, (key,)) for name in ('get', 'remove') for key in (0, 1))
        sequences = 0
        for length in range(1, 5):
            for commands in product(operations, repeat=length):
                instance, reference = MyHashMap(), []
                for command in commands:
                    self.apply(instance, reference, command)
                    for key in (0, 1, 1000000):
                        self.apply(instance, reference, ('get', (key,)))
                sequences += 1
        self.assertEqual(sequences, 4680)

    def test_collision_overwrites_zero_values_and_exact_10000_calls(self):
        keys = [1009 * index for index in range(992)] + [1000000]
        commands = [('put', (key, index % 2 * 1000000)) for index, key in enumerate(keys)]
        names = ('get', 'remove', 'put', 'put', 'get', 'remove', 'put')
        while len(commands) < 9007:
            position = len(commands)
            name = names[position % len(names)]
            key = keys[(position * 37) % len(keys)]
            arguments = (key, (position * 997) % 1000001) if name == 'put' else (key,)
            commands.append((name, arguments))
        commands += [('get', (key,)) for key in keys]
        self.assertEqual(len(commands), 10000)
        self.assertTrue(all(0 <= key <= 1000000 for key in keys))
        instance, reference = MyHashMap(), []
        for command in commands:
            self.apply(instance, reference, command)


if __name__ == '__main__':
    unittest.main()
