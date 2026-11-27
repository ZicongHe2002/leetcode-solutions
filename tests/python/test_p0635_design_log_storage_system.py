import random
import unittest

from python.p0635_design_log_storage_system import LogSystem


GRANULARITIES = ('Year', 'Month', 'Day', 'Hour', 'Minute', 'Second')


def timestamp(parts):
    return ':'.join(f'{value:04d}' if index == 0 else f'{value:02d}'
                    for index, value in enumerate(parts))


def random_parts(rng):
    return (rng.randint(2000, 2017), rng.randint(1, 12), rng.randint(1, 31),
            rng.randrange(24), rng.randrange(60), rng.randrange(60))


class LogStorageTests(unittest.TestCase):
    def test_five_hundred_calls_against_integer_tuple_filter(self):
        rng = random.Random(635)
        store = LogSystem()
        records = [(id, random_parts(rng)) for id in range(1, 151)]
        for id, parts in records:
            self.assertIsNone(store.put(id, timestamp(parts)))
        for index in range(350):
            lower, upper = sorted((random_parts(rng), random_parts(rng)))
            depth = index % 6 + 1
            expected = [id for id, parts in records
                        if lower[:depth] <= parts[:depth] <= upper[:depth]]
            actual = store.retrieve(timestamp(lower), timestamp(upper), GRANULARITIES[depth - 1])
            self.assertIs(type(actual), list)
            self.assertEqual(sorted(actual), expected)

    def test_empty_inclusive_boundaries_and_repeat_queries(self):
        store = LogSystem()
        start, end = '2000:01:01:00:00:00', '2017:12:31:23:59:59'
        self.assertEqual(store.retrieve(start, end, 'Year'), [])
        for id, value in ((1, end), (2, start), (3, '2017:01:01:00:00:00'),
                          (4, '2017:01:01:23:59:59'), (5, '2017:01:02:00:00:00')):
            store.put(id, value)
        lower, upper = '2017:01:01:23:59:58', '2017:01:01:23:59:59'
        for _ in range(2):
            self.assertEqual(sorted(store.retrieve(lower, upper, 'Day')), [3, 4])
            self.assertEqual(store.retrieve(lower, upper, 'Second'), [4])
            self.assertEqual(sorted(store.retrieve(start, end, 'Year')), [1, 2, 3, 4, 5])

    def test_maximum_calls_preserve_all_ids_at_one_timestamp(self):
        store = LogSystem()
        for id in range(1, 500):
            store.put(id, '2017:12:31:00:00:00')
        result = store.retrieve('2017:12:31:23:59:59', '2017:12:31:23:59:59', 'Day')
        self.assertEqual(result, list(range(1, 500)))


if __name__ == '__main__':
    unittest.main()
