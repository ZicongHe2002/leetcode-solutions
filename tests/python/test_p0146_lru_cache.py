import unittest
from collections import OrderedDict
from itertools import product

from python.p0146_lru_cache import LRUCache


def model_put(model, capacity, key, value):
    model[key] = value
    model.move_to_end(key)
    if len(model) > capacity:
        model.popitem(last=False)


def model_get(model, key):
    if key not in model:
        return -1
    model.move_to_end(key)
    return model[key]


class LruCacheTests(unittest.TestCase):
    def test_all_short_programs_against_ordered_dictionary(self):
        actions = [('get', key) for key in range(4)] + [('put', key, key + 1) for key in range(4)] + [('put', 0, 5)]
        programs = 0
        for capacity in range(1, 4):
            for size in range(5):
                for operations in product(actions, repeat=size):
                    cache, model = LRUCache(capacity), OrderedDict()
                    for action in operations:
                        if action[0] == 'put':
                            self.assertIsNone(cache.put(action[1], action[2]))
                            model_put(model, capacity, action[1], action[2])
                        else:
                            result = cache.get(action[1])
                            self.assertIs(type(result), int)
                            self.assertEqual(result, model_get(model, action[1]))
                    programs += 1
        self.assertEqual(programs, 22143)

    def test_maximum_capacity_operation_count_key_and_value_boundaries(self):
        cache, model = LRUCache(3000), OrderedDict()
        for index in range(100000):
            key, value = index % 10001, 100000 if index % 2 else 0
            self.assertIsNone(cache.put(key, value))
            model_put(model, 3000, key, value)
            query = index * 17 % 10001
            self.assertEqual(cache.get(query), model_get(model, query))


if __name__ == '__main__':
    unittest.main()
