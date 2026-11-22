import unittest
from collections import Counter
from itertools import combinations

from python.p0136_single_number import Solution


def unique_orders(counts, length, prefix=()):
    if len(prefix) == length:
        yield prefix
        return
    for value in counts:
        if counts[value]:
            counts[value] -= 1
            yield from unique_orders(counts, length, prefix + (value,))
            counts[value] += 1


class SingleNumberTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        singletons = [value for value, count in Counter(values).items() if count == 1]
        self.assertEqual(len(singletons), 1)
        self.assertEqual(Solution().singleNumber(values), singletons[0])
        self.assertEqual(values, before)

    def test_all_small_pair_subsets_and_unique_orders_against_counter(self):
        checks = 0
        pool = [-1, 0, 1, 2]
        for singleton in pool:
            others = [value for value in pool if value != singleton]
            for pair_count in range(4):
                for paired in combinations(others, pair_count):
                    counts = {singleton: 1, **{value: 2 for value in paired}}
                    for order in unique_orders(counts, 2 * pair_count + 1):
                        self.check(list(order))
                        checks += 1
        self.assertEqual(checks, 2920)

    def test_maximum_legal_odd_length_negative_values_and_singletons(self):
        self.check([value for value in range(-15000, -1) for _ in range(2)] + [30000])
        self.check([-30000] + [value for value in range(14999) for _ in range(2)])
        self.check([0])
        self.check([-30000])


if __name__ == '__main__':
    unittest.main()
