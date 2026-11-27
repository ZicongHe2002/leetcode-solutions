import random
import unittest

from python.p0762_prime_number_of_set_bits_in_binary_representation import Solution


def text_count_and_trial_division(value):
    count = format(value, 'b').count('1')
    return count >= 2 and all(count % divisor for divisor in range(2, count))


class PrimeSetBitsTests(unittest.TestCase):
    def check(self, left, right, expected=None):
        result = Solution().countPrimeSetBits(left, right)
        self.assertIs(type(result), int)
        self.assertEqual(result, sum(text_count_and_trial_division(value) for value in range(left, right + 1))
                         if expected is None else expected, (left, right))

    def test_all_small_closed_intervals_against_binary_text_and_trial_divisors(self):
        checked = 0
        for left in range(1, 128):
            for right in range(left, 128):
                self.check(left, right)
                checked += 1
        self.assertEqual(checked, 8128)

    def test_seeded_full_domain_official_examples_and_maximum_width(self):
        rng = random.Random(762)
        for _ in range(100):
            left = rng.randrange(1, 10**6 + 1)
            right = min(10**6, left + rng.randrange(10001))
            self.check(left, right)
        self.check(990000, 10**6)
        self.check(10**6, 10**6)
        self.check(6, 10, 4)
        self.check(10, 15, 5)
        self.check(1, 1, 0)
        self.check(2**19 - 1, 2**19 - 1, 1)
        for bit in range(20):
            self.check(1 << bit, 1 << bit, 0)


if __name__ == '__main__':
    unittest.main()
