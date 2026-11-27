import unittest
from itertools import product

from python.p0677_map_sum_pairs import MapSum


def scan_sum(values, prefix):
    return sum(value for key, value in values.items() if key.startswith(prefix))


class MapSumPairsTests(unittest.TestCase):
    def test_all_short_insert_programs_against_dictionary_prefix_scan(self):
        choices = tuple(product(('a', 'ab', 'b'), (1, 2, 5)))
        checked = 0
        for program in product(choices, repeat=3):
            obj, values = MapSum(), {}
            for key, value in program:
                self.assertIsNone(obj.insert(key, value))
                values[key] = value
                for prefix in ('a', 'ab', 'b', 'ba', 'aa', 'c'):
                    result = obj.sum(prefix)
                    self.assertIs(type(result), int)
                    self.assertEqual(result, scan_sum(values, prefix), (program, prefix))
                    checked += 1
        self.assertEqual(checked, 13122)

    def test_fifty_calls_maximum_key_length_values_and_key_prefix_overlap(self):
        obj, values = MapSum(), {}
        calls = 0
        for i in range(25):
            key = 'a' * 49 + chr(97 + i % 5)
            value = 1000 if i % 2 == 0 else 1
            obj.insert(key, value)
            values[key] = value
            prefix = ('a', 'a' * 49, key, 'z', 'a' * 50)[i % 5]
            self.assertEqual(obj.sum(prefix), scan_sum(values, prefix))
            calls += 2
        self.assertEqual(calls, 50)
        other = MapSum()
        self.assertEqual(other.sum('app'), 0)
        other.insert('apple', 3)
        other.insert('app', 2)
        self.assertEqual(other.sum('ap'), 5)
        other.insert('apple', 1)
        self.assertEqual(other.sum('app'), 3)
        other.insert('app', 2)
        self.assertEqual(other.sum('apple'), 1)


if __name__ == '__main__':
    unittest.main()
