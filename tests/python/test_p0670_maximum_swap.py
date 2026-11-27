import random
import unittest

from python.p0670_maximum_swap import Solution


def all_swaps(number):
    digits = list(str(number))
    best = number
    for first in range(len(digits)):
        for second in range(first + 1, len(digits)):
            candidate = digits[:]
            candidate[first], candidate[second] = candidate[second], candidate[first]
            best = max(best, int(''.join(candidate)))
    return best


class MaximumSwapTests(unittest.TestCase):
    def check(self, number, expected=None):
        result = Solution().maximumSwap(number)
        self.assertIs(type(result), int)
        self.assertEqual(result, all_swaps(number) if expected is None else expected, number)

    def test_all_numbers_through_one_hundred_thousand_against_actual_swaps(self):
        for number in range(100001):
            self.check(number)

    def test_large_seeded_inputs_repeated_digits_and_no_swap_boundaries(self):
        for number, expected in ((0, 0), (1, 1), (2736, 7236), (9973, 9973),
                                 (1993, 9913), (98368, 98863), (100000000, 100000000),
                                 (99999999, 99999999), (109090, 909010)):
            self.check(number, expected)
        rng = random.Random(670)
        for _ in range(1000):
            self.check(rng.randrange(100000001))


if __name__ == '__main__':
    unittest.main()
