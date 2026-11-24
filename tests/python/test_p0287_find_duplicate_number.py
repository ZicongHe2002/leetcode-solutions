import unittest
from collections import Counter
from itertools import product

from python.p0287_find_duplicate_number import Solution


class DuplicateNumberTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        repeated = [value for value, count in Counter(values).items() if count > 1]
        self.assertEqual(len(repeated), 1)
        self.assertEqual(Solution().findDuplicate(values), repeated[0])
        self.assertEqual(values, before)

    def test_all_small_legal_arrays_against_frequency_oracle(self):
        checks = 0
        for n in range(1, 6):
            for values in product(range(1, n + 1), repeat=n + 1):
                if sum(count > 1 for count in Counter(values).values()) == 1:
                    self.check(list(values))
                    checks += 1
        self.assertEqual(checks, 5841)

    def test_maximum_length_duplicate_positions_and_repeated_more_than_twice(self):
        for duplicate in [1, 50000, 100000]:
            self.check(list(range(1, 100001)) + [duplicate])
        self.check([100000] * 100001)
        self.check([1, 1])
        self.check([3, 3, 3, 3, 3])


if __name__ == '__main__':
    unittest.main()
