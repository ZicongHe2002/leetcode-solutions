import random
import unittest

from python.p0660_remove_9 import Solution


def decimal_rank(bound):
    counts = {True: 1}
    for character in str(bound):
        actual = int(character)
        following = {}
        for tight, count in counts.items():
            for digit in range((actual if tight else 9) + 1):
                if digit == 9:
                    continue
                next_tight = tight and digit == actual
                following[next_tight] = following.get(next_tight, 0) + count
        counts = following
    return sum(counts.values()) - 1


class RemoveNineTests(unittest.TestCase):
    def test_first_hundred_thousand_entries_against_direct_decimal_filter(self):
        rank = 0
        value = 1
        while rank < 100000:
            if '9' not in str(value):
                rank += 1
                actual = Solution().newInteger(rank)
                self.assertIs(type(actual), int)
                self.assertEqual(actual, value, rank)
            value += 1

    def test_large_ranks_and_radix_carries_against_decimal_digit_count(self):
        boundary = {1, 8, 9, 10, 800000000}
        for exponent in range(1, 10):
            boundary.update(value for value in (9**exponent - 1, 9**exponent, 9**exponent + 1)
                            if 1 <= value <= 800000000)
        rng = random.Random(660)
        for rank in sorted(boundary) + [rng.randint(1, 800000000) for _ in range(1000)]:
            actual = Solution().newInteger(rank)
            self.assertIs(type(actual), int)
            self.assertNotIn('9', str(actual))
            self.assertEqual(decimal_rank(actual), rank)
            self.assertEqual(decimal_rank(actual - 1), rank - 1)


if __name__ == '__main__':
    unittest.main()
