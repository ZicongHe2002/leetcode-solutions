from collections import Counter
from functools import lru_cache
from itertools import product
import random
import unittest
from unittest.mock import patch

import python.p0324_wiggle_sort_ii as implementation


@lru_cache(None)
def can_wiggle(values):
    counts = Counter(values)

    def arrange(prefix):
        if len(prefix) == len(values):
            return True
        for value in counts:
            allowed = not prefix or (prefix[-1] < value if len(prefix) % 2 else prefix[-1] > value)
            if counts[value] and allowed:
                counts[value] -= 1
                result = arrange(prefix + (value,))
                counts[value] += 1
                if result:
                    return True
        return False

    return arrange(())


class StrictInPlaceWiggleTests(unittest.TestCase):
    def check(self, values):
        before = Counter(values)
        result = implementation.Solution().wiggleSort(values)
        self.assertIsNone(result)
        self.assertEqual(Counter(values), before)
        self.assertTrue(all((values[index] < values[index + 1] if index % 2 == 0
                             else values[index] > values[index + 1])
                            for index in range(len(values) - 1)))

    def test_all_small_feasible_inputs_with_three_pivot_strategies(self):
        total = 0
        selectors = (lambda start, stop: start, lambda start, stop: stop - 1,
                     random.Random(324).randrange)
        for selector in selectors:
            checks = 0
            with patch.object(implementation, 'randrange', selector):
                for size in range(1, 8):
                    for values in product(range(3), repeat=size):
                        if can_wiggle(tuple(sorted(values))):
                            self.check(list(values))
                            checks += 1
            self.assertEqual(checks, 2093)
            total += checks
        self.assertEqual(total, 6279)

    def test_maximum_length_duplicate_placement_and_value_limits(self):
        with patch.object(implementation, 'randrange', random.Random(324).randrange):
            self.check([0] * 25000 + [5000] * 25000)
            self.check([0] * 25000 + [5000] * 24999)
            self.check(list(range(5000, -1, -1)))
            self.check([5000])
            self.check([1, 5, 1, 1, 6, 4])


if __name__ == '__main__':
    unittest.main()
