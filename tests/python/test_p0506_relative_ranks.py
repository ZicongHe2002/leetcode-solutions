from itertools import permutations
import unittest

from python.p0506_relative_ranks import Solution


def higher_score_count_oracle(scores):
    medals = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
    result = []
    for score in scores:
        rank = 1 + sum(other > score for other in scores)
        result.append(medals.get(rank, str(rank)))
    return result


class RankOriginalIndexTests(unittest.TestCase):
    def check(self, scores, expected=None):
        before = scores[:]
        actual = Solution().findRelativeRanks(scores)
        self.assertIs(type(actual), list)
        self.assertTrue(all(type(rank) is str for rank in actual))
        self.assertEqual(actual, higher_score_count_oracle(scores) if expected is None else expected)
        self.assertEqual(scores, before)

    def test_all_small_distinct_score_orders_against_higher_score_counts(self):
        arrays = 0
        for size in range(7):
            for scores in permutations(range(6), size):
                self.check(list(scores))
                arrays += 1
        self.assertEqual(arrays, 1957)

    def test_maximum_count_value_boundaries_medal_positions_and_empty_extension(self):
        scores = [100 * index for index in range(10000)]
        expected = [str(rank) for rank in range(10000, 3, -1)] + ['Bronze Medal', 'Silver Medal', 'Gold Medal']
        self.check(scores, expected)
        self.check([1000000, 0, 5], ['Gold Medal', 'Bronze Medal', 'Silver Medal'])
        self.check([10, 3, 8, 9, 4], ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4'])
        self.check([0], ['Gold Medal'])
        self.check([], [])


if __name__ == '__main__':
    unittest.main()
