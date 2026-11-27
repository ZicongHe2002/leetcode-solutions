import unittest
from itertools import product

from python.p0784_letter_case_permutation import Solution


class LetterCasePermutationTests(unittest.TestCase):
    def check(self, text, expected=None):
        result = Solution().letterCasePermutation(text)
        self.assertIs(type(result),list)
        self.assertTrue(all(type(value) is str for value in result))
        self.assertEqual(len(result),len(set(result)))
        self.assertTrue(all(len(value)==len(text) and value.lower()==text.lower() for value in result))
        if expected is not None:
            self.assertEqual(set(result),expected,text)
        else:
            self.assertEqual(len(result),1 << sum(char.isalpha() for char in text))

    def test_every_small_input_against_complete_whole_text_case_equivalence_classes(self):
        checked = 0
        for size in range(1,6):
            texts = [''.join(chars) for chars in product('aAbB01',repeat=size)]
            groups = {}
            for text in texts:
                groups.setdefault(text.lower(),set()).add(text)
            for text in texts:
                self.check(text,groups[text.lower()])
                checked += 1
        self.assertEqual(checked,9330)

    def test_official_examples_maximum_letters_digit_only_and_leading_zero(self):
        self.check('a1b2',{'a1b2','a1B2','A1b2','A1B2'})
        self.check('3z4',{'3z4','3Z4'})
        self.check('aBcDeFgHiJkL')
        self.check('a' * 12)
        self.check('012345678901',{'012345678901'})
        self.check('0a',{'0a','0A'})


if __name__ == '__main__':
    unittest.main()
