import unittest

from python.p0390_elimination_game import Solution


def list_deletion_oracle(size):
    values = list(range(1, size + 1))
    from_left = True
    while len(values) > 1:
        values = values[1::2] if from_left else values[::-1][1::2][::-1]
        from_left = not from_left
    return values[0]


def mirrored_rank_oracle(size):
    if size == 1:
        return 1
    return 2 * (1 + size // 2 - mirrored_rank_oracle(size // 2))


class EliminationProgressionTests(unittest.TestCase):
    def test_every_small_size_against_actual_list_deletion(self):
        for size in range(1, 2001):
            actual = Solution().lastRemaining(size)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, list_deletion_oracle(size))

    def test_rank_recurrence_power_boundaries_and_maximum_size(self):
        for exponent in range(1, 30):
            for size in (2**exponent - 1, 2**exponent, 2**exponent + 1):
                self.assertEqual(Solution().lastRemaining(size), mirrored_rank_oracle(size))
        self.assertEqual(Solution().lastRemaining(9), 6)
        self.assertEqual(Solution().lastRemaining(10**9), mirrored_rank_oracle(10**9))


if __name__ == '__main__':
    unittest.main()
