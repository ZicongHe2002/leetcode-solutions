import unittest

from python.p0544_output_contest_matches import Solution


def complementary_seed_leaf_order_oracle(n):
    seeds = [1]
    while len(seeds) < n:
        size = 2 * len(seeds)
        seeds = [value for seed in seeds for value in (seed, size + 1 - seed)]

    def bracket(start, end):
        if end - start == 1:
            return str(seeds[start])
        middle = (start + end) // 2
        return '(' + bracket(start, middle) + ',' + bracket(middle, end) + ')'

    return bracket(0, n)


class RankedTournamentStringTests(unittest.TestCase):
    def test_every_legal_team_count_against_complementary_leaf_construction(self):
        for exponent in range(1, 13):
            n = 1 << exponent
            actual = Solution().findContestMatch(n)
            self.assertIs(type(actual), str)
            self.assertEqual(actual, complementary_seed_leaf_order_oracle(n))

    def test_known_brackets_and_maximum_full_grammar_seed_rounds_and_coverage(self):
        self.assertEqual(Solution().findContestMatch(2), '(1,2)')
        self.assertEqual(Solution().findContestMatch(4), '((1,4),(2,3))')
        self.assertEqual(Solution().findContestMatch(8), '(((1,8),(4,5)),((2,7),(3,6)))')
        n = 4096
        text = Solution().findContestMatch(n)
        position = 0
        leaves = []

        def parse():
            nonlocal position
            if text[position] != '(':
                start = position
                while position < len(text) and text[position].isdigit():
                    position += 1
                self.assertGreater(position, start)
                seed = int(text[start:position])
                leaves.append(seed)
                return seed, 0
            position += 1
            left, left_height = parse()
            self.assertEqual(text[position], ',')
            position += 1
            right, right_height = parse()
            self.assertEqual(text[position], ')')
            position += 1
            self.assertEqual(left_height, right_height)
            height = left_height + 1
            self.assertLess(left, right)
            self.assertEqual(left + right, n // (1 << (height - 1)) + 1)
            return left, height

        self.assertEqual(parse(), (1, 12))
        self.assertEqual(position, len(text))
        self.assertEqual(sorted(leaves), list(range(1, n + 1)))


if __name__ == '__main__':
    unittest.main()
