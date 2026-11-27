from functools import lru_cache
from itertools import combinations_with_replacement
from math import prod
import random
import unittest

from python.p0625_minimum_factorization import Solution


@lru_cache(None)
def exhaustive_minimum_product_table():
    minimums = {1: 1}
    candidates = 0
    for size in range(1, 10):
        for digits in combinations_with_replacement(range(2, 10), size):
            number = int(''.join(map(str, digits)))
            product = prod(digits)
            minimums[product] = min(minimums.get(product, number), number)
            candidates += 1
    assert candidates == 24309
    return minimums


class MinimumFactorizationTests(unittest.TestCase):
    def check(self, num, expected):
        result = Solution().smallestFactorization(num)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, num)
        self.assertTrue(0 <= result <= 2**31 - 1)
        if result:
            self.assertEqual(prod(map(int, str(result))), num)

    def test_small_inputs_all_possible_answer_products_and_seeded_large_inputs(self):
        minimums = exhaustive_minimum_product_table()
        for num in range(1, 100001):
            self.check(num, minimums.get(num, 0))
        for num, expected in minimums.items():
            self.assertLessEqual(num, 2**31 - 1)
            self.check(num, expected)
        rng = random.Random(625)
        for _ in range(1000):
            num = rng.randint(1, 2**31 - 1)
            self.check(num, minimums.get(num, 0))

    def test_one_prime_failure_greedy_exchanges_and_nine_ten_digit_boundary(self):
        for num, expected in ((1, 1), (9, 9), (48, 68), (15, 35), (16, 28), (18, 29),
                              (24, 38), (36, 49), (12, 26), (100, 455), (11, 0), (13, 0),
                              (2**27, 888888888), (2**28, 0), (2**29, 0), (2**30, 0),
                              (3**18, 999999999), (3**19, 0), (7**9, 777777777), (7**10, 0),
                              (2**31 - 1, 0)):
            self.check(num, expected)


if __name__ == '__main__':
    unittest.main()
