import unittest
from itertools import combinations, product

from python.p0792_number_of_matching_subsequences import Solution


def actual_subsequence_strings(text):
    return {''.join(text[index] for index in chosen)
            for size in range(len(text) + 1)
            for chosen in combinations(range(len(text)),size)}


class MatchingSubsequencesTests(unittest.TestCase):
    def check(self, text, words, expected):
        before = words[:]
        result = Solution().numMatchingSubseq(text,words)
        self.assertIs(type(result),int)
        self.assertEqual(result,expected,(text,words))
        self.assertEqual(words,before)

    def test_all_small_sources_and_words_against_actual_index_combinations(self):
        words = [''.join(chars) for size in range(1,6) for chars in product('ab',repeat=size)]
        sources = queries = 0
        for size in range(1,10):
            for chars in product('ab',repeat=size):
                text = ''.join(chars)
                actual = actual_subsequence_strings(text)
                for word in words:
                    self.check(text,[word],int(word in actual))
                    queries += 1
                batch = words + ['a','aa','a']
                self.check(text,batch,sum(word in actual for word in batch))
                sources += 1
        self.assertEqual((sources,queries),(1022,63364))

    def test_examples_same_character_bucket_and_all_legal_size_limits(self):
        self.check('abcde',['a','bb','acd','ace'],3)
        self.check('dsahjpjauf',['ahjpjau','ja','ahbwzgqnuk','tnmlanowax'],2)
        self.check('a',['a','aa','aaa','a'],2)
        self.check('a' * 50000,['a' * 50] * 5000,5000)
        self.check('a' * 50000,['a' * 49 + 'b'] * 5000,0)
        self.check('ab' * 25000,['ba' * 25] * 2500 + ['z' * 50] * 2500,2500)


if __name__ == '__main__':
    unittest.main()
