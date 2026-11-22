from functools import lru_cache
import unittest

from python.p0375_guess_number_higher_or_lower_ii import Solution


@lru_cache(None)
def all_search_policies(left, right):
    if left > right:
        return (None,)
    return tuple((guess, lower, upper)
                 for guess in range(left, right + 1)
                 for lower in all_search_policies(left, guess - 1)
                 for upper in all_search_policies(guess + 1, right))


def worst_wrong_guess_cost(policy):
    guess, lower, upper = policy
    outcomes = [0]
    if lower is not None:
        outcomes.append(guess + worst_wrong_guess_cost(lower))
    if upper is not None:
        outcomes.append(guess + worst_wrong_guess_cost(upper))
    return max(outcomes)


class GuessingDecisionTreeOracleTests(unittest.TestCase):
    def test_small_domains_against_every_comparison_policy(self):
        policies = 0
        for n in range(1, 9):
            candidates = all_search_policies(1, n)
            expected = min(map(worst_wrong_guess_cost, candidates))
            result = Solution().getMoneyAmount(n)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected)
            policies += len(candidates)
        self.assertEqual(policies, 2055)

    def test_maximum_domain_free_correct_guess_and_repeated_calls(self):
        solution = Solution()
        for n, expected in ((1, 0), (2, 1), (3, 2), (10, 16), (200, 952), (1, 0)):
            result = solution.getMoneyAmount(n)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
