from itertools import accumulate, product
import unittest

from python.p0301_remove_invalid_parentheses import Solution


def deletion_subset_oracle(text):
    parentheses = [index for index, character in enumerate(text) if character in '()']
    best = len(parentheses) + 1
    answers = set()
    for mask in range(1 << len(parentheses)):
        count = mask.bit_count()
        if count > best:
            continue
        removed = {position for bit, position in enumerate(parentheses) if mask & (1 << bit)}
        candidate = ''.join(character for index, character in enumerate(text) if index not in removed)
        prefix = [0] + list(accumulate(1 if character == '(' else -1 if character == ')' else 0 for character in candidate))
        if min(prefix) >= 0 and prefix[-1] == 0:
            if count < best:
                answers.clear()
                best = count
            answers.add(candidate)
    return answers


class MinimumParenthesisDeletionTests(unittest.TestCase):
    def check(self, text, expected=None):
        result = Solution().removeInvalidParentheses(text)
        self.assertIs(type(result), list)
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(set(result), deletion_subset_oracle(text) if expected is None else expected)
        letters = ''.join(character for character in text if character not in '()')
        self.assertTrue(all(''.join(character for character in answer if character not in '()') == letters for answer in result))

    def test_all_small_strings_against_minimum_deletion_subsets(self):
        strings = 0
        for size in range(8):
            for characters in product('()a', repeat=size):
                self.check(''.join(characters))
                strings += 1
        self.assertEqual(strings, 3280)

    def test_multiple_answers_letters_repeated_runs_and_contract_boundaries(self):
        self.check('(a)())()', {'(a())()', '(a)()()'})
        self.check('abc', {'abc'})
        self.check(')' * 20 + 'abcde', {'abcde'})
        self.check('(' * 10 + ')' * 10 + 'abcde', {'(' * 10 + ')' * 10 + 'abcde'})
        self.check(')(' * 10 + 'abcde', {'()' * 9 + 'abcde'})
        self.check('', {''})


if __name__ == '__main__':
    unittest.main()
