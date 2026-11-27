import unittest

from python.p0400_nth_digit import Solution


def digits_through(number):
    total = 0
    for width in range(1, len(str(number)) + 1):
        lower, upper = 10**(width - 1), 10**width - 1
        total += max(0, min(number, upper) - lower + 1) * width
    return total


def rank_binary_search_oracle(position):
    lower, upper = 1, position
    while lower < upper:
        middle = (lower + upper) // 2
        if digits_through(middle) >= position:
            upper = middle
        else:
            lower = middle + 1
    offset = position - digits_through(lower - 1) - 1
    return int(str(lower)[offset])


class DigitBlockPositionTests(unittest.TestCase):
    def test_every_position_in_small_materialized_digit_stream(self):
        stream = ''.join(map(str, range(1, 10000)))
        self.assertEqual(len(stream), 38889)
        for position, character in enumerate(stream, 1):
            actual = Solution().findNthDigit(position)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, int(character))

    def test_decimal_block_edges_and_large_ranks_against_binary_search(self):
        boundaries = (9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889)
        for last in boundaries:
            self.assertEqual(Solution().findNthDigit(last), 9)
            self.assertEqual(Solution().findNthDigit(last + 1), 1)
            self.assertEqual(Solution().findNthDigit(last + 2), 0)
            for position in (last - 1, last, last + 1, last + 2):
                self.assertEqual(Solution().findNthDigit(position), rank_binary_search_oracle(position))
        for position in (10**9, 1234567890, 2**31 - 1):
            self.assertEqual(Solution().findNthDigit(position), rank_binary_search_oracle(position))


if __name__ == '__main__':
    unittest.main()
