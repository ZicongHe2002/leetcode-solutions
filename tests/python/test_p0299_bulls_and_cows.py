from itertools import product
import unittest

from python.p0299_bulls_and_cows import Solution


def matching_search_oracle(secret, guess):
    bulls = sum(first == second for first, second in zip(secret, guess))
    first = [a for a, b in zip(secret, guess) if a != b]
    second = [b for a, b in zip(secret, guess) if a != b]

    def maximum_pairs(index, used):
        if index == len(first):
            return 0
        best = maximum_pairs(index + 1, used)
        for other, value in enumerate(second):
            if not used & (1 << other) and value == first[index]:
                best = max(best, 1 + maximum_pairs(index + 1, used | (1 << other)))
        return best

    return f'{bulls}A{maximum_pairs(0, 0)}B'


class BullsAndCowsMatchingTests(unittest.TestCase):
    def test_all_small_string_pairs_against_explicit_matching_search(self):
        pairs = 0
        for size in range(1, 5):
            strings = [''.join(chars) for chars in product('012', repeat=size)]
            for secret, guess in product(strings, repeat=2):
                self.assertEqual(Solution().getHint(secret, guess), matching_search_oracle(secret, guess))
                pairs += 1
        self.assertEqual(pairs, 7380)

    def test_duplicate_reuse_leading_zeroes_and_maximum_lengths(self):
        solver = Solution()
        self.assertEqual(solver.getHint('1807', '7810'), '1A3B')
        self.assertEqual(solver.getHint('1123', '0111'), '1A1B')
        self.assertEqual(solver.getHint('0' * 1000, '0' * 1000), '1000A0B')
        self.assertEqual(solver.getHint('0' * 1000, '1' * 1000), '0A0B')
        self.assertEqual(solver.getHint('0' * 500 + '1' * 500, '1' * 500 + '0' * 500), '0A1000B')
        self.assertEqual(solver.getHint('', ''), '0A0B')


if __name__ == '__main__':
    unittest.main()
