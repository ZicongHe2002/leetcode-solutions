from itertools import product
from random import Random
import unittest

from python.p0460_lfu_cache import LFUCache


class ScanningLfuModel:
    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = {}
        self.clock = 0

    def get(self, key):
        self.clock += 1
        if key not in self.entries:
            return -1
        value, frequency, _ = self.entries[key]
        self.entries[key] = (value, frequency + 1, self.clock)
        return value

    def put(self, key, value):
        self.clock += 1
        if self.capacity == 0:
            return
        if key in self.entries:
            _, frequency, _ = self.entries[key]
            self.entries[key] = (value, frequency + 1, self.clock)
            return
        if len(self.entries) == self.capacity:
            victim = min(self.entries, key=lambda candidate: (self.entries[candidate][1], self.entries[candidate][2]))
            del self.entries[victim]
        self.entries[key] = (value, 1, self.clock)


class FrequencyBucketLruTests(unittest.TestCase):
    def verify(self, cache, model):
        self.assertEqual(cache.entries, {key: (value, frequency) for key, (value, frequency, _) in model.entries.items()})
        expected_minimum = min((item[1] for item in model.entries.values()), default=0)
        self.assertEqual(cache.minimum, expected_minimum)
        seen = set()
        for frequency, bucket in cache.buckets.items():
            self.assertTrue(bucket)
            expected_keys = [key for key, item in model.entries.items() if item[1] == frequency]
            expected_keys.sort(key=lambda key: model.entries[key][2])
            self.assertEqual(list(bucket), expected_keys)
            self.assertFalse(seen.intersection(bucket))
            seen.update(bucket)
        self.assertEqual(seen, set(model.entries))
        self.assertLessEqual(len(cache.buckets), len(cache.entries))

    def step(self, cache, model, operation, inspect=True):
        method, *arguments = operation
        self.assertEqual(getattr(cache, method)(*arguments), getattr(model, method)(*arguments))
        if inspect:
            self.verify(cache, model)

    def test_every_short_program_against_timestamp_scanning_model(self):
        actions = (('get', 0), ('get', 1), ('put', 0, 0), ('put', 1, 7), ('put', 2, 3))
        programs = 0
        for capacity in range(4):
            for length in range(7):
                for operations in product(actions, repeat=length):
                    cache, model = LFUCache(capacity), ScanningLfuModel(capacity)
                    self.verify(cache, model)
                    for operation in operations:
                        self.step(cache, model, operation)
                    programs += 1
        self.assertEqual(programs, 78124)

    def test_updates_maximum_capacity_boundaries_and_maximum_call_count(self):
        generator = Random(460)
        for capacity in range(6):
            cache, model = LFUCache(capacity), ScanningLfuModel(capacity)
            for _ in range(500):
                key = generator.randrange(9)
                operation = ('get', key) if generator.randrange(2) else ('put', key, generator.randrange(10**9 + 1))
                self.step(cache, model, operation)
        cache, model = LFUCache(10000), ScanningLfuModel(10000)
        for key in range(10000):
            self.step(cache, model, ('put', key, key), False)
        for key in range(1, 10000):
            self.step(cache, model, ('get', key), False)
        self.verify(cache, model)
        for operation in (('put', 100000, 10**9), ('get', 0), ('put', 100000, 0),
                          ('get', 100000), ('put', 99999, 5), ('get', 1)):
            self.step(cache, model, operation)
        cache, model = LFUCache(1), ScanningLfuModel(1)
        self.step(cache, model, ('put', 0, 0))
        for _ in range(199999):
            self.step(cache, model, ('get', 0), False)
        self.verify(cache, model)
        self.assertEqual(len(cache.buckets), 1)


if __name__ == '__main__':
    unittest.main()
