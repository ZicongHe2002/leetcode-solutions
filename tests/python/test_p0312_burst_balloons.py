from functools import lru_cache
from itertools import product
import unittest

from python.p0312_burst_balloons import Solution


@lru_cache(None)
def first_burst_oracle(values):
    if not values:
        return 0
    return max((values[index - 1] if index else 1) * value
               * (values[index + 1] if index + 1 < len(values) else 1)
               + first_burst_oracle(values[:index] + values[index + 1:])
               for index, value in enumerate(values))


class BurstBalloonsFirstChoiceOracleTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = first_burst_oracle(tuple(values))
        result = Solution().maxCoins(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_every_small_array_against_first_burst_state_search(self):
        checked = 0
        for size in range(1, 7):
            for values in product((0, 1, 2), repeat=size):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 1092)

    def test_maximum_length_zero_balloons_and_maximum_values(self):
        self.check([100] * 300, 298 * 100**3 + 100**2 + 100)
        self.check([0] * 300, 0)
        self.check([0, 100] * 150, 148 * 100**3 + 100**2 + 100)
        self.check([3, 1, 5, 8], 167)
        self.check([100], 100)
        self.check([0], 0)


if __name__ == '__main__':
    unittest.main()
