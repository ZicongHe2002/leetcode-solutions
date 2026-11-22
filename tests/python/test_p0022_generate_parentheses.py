import unittest
from itertools import product

from python.p0022_generate_parentheses import Solution


def all_strings_oracle(n):
    result = []
    for characters in product('()', repeat=2 * n):
        balance = 0
        for character in characters:
            balance += 1 if character == '(' else -1
            if balance < 0:
                break
        else:
            if balance == 0:
                result.append(''.join(characters))
    return result


class ParenthesesTests(unittest.TestCase):
    def check(self, n):
        actual = Solution().generateParenthesis(n)
        self.assertEqual(sorted(actual), sorted(all_strings_oracle(n)))
        for expression in actual:
            self.assertEqual(len(expression), 2 * n)
            self.assertEqual(expression.count('('), n)
            self.assertEqual(expression.count(')'), n)
            balance = 0
            for character in expression:
                balance += 1 if character == '(' else -1
                self.assertGreaterEqual(balance, 0)
            self.assertEqual(balance, 0)
        return actual

    def test_small_pair_counts_against_all_candidate_strings(self):
        for n in range(8):
            self.check(n)

    def test_maximum_pair_count_and_explicit_small_answers(self):
        self.assertEqual(len(self.check(8)), 1430)
        self.assertEqual(Solution().generateParenthesis(1), ['()'])
        self.assertEqual(sorted(Solution().generateParenthesis(2)), ['(())', '()()'])
        self.assertEqual(Solution().generateParenthesis(0), [''])


if __name__ == '__main__':
    unittest.main()
