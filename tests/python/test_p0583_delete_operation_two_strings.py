import unittest
from itertools import combinations, product

from python.p0583_delete_operation_two_strings import Solution


def all_subsequences(word):
    return {''.join(word[index] for index in chosen)
            for size in range(len(word) + 1)
            for chosen in combinations(range(len(word)), size)}


class DeleteDistanceTests(unittest.TestCase):
    def check(self, left, right, expected):
        result = Solution().minDistance(left, right)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_binary_words_and_empty_extensions_against_subsequence_sets(self):
        words = [''.join(chars) for size in range(5) for chars in product('ab', repeat=size)]
        subsequences = {word: all_subsequences(word) for word in words}
        checks = 0
        for left in words:
            for right in words:
                longest = max(map(len, subsequences[left] & subsequences[right]))
                self.check(left, right, len(left) + len(right) - 2 * longest)
                checks += 1
        self.assertEqual(checks, 961)

    def test_maximum_lengths_deletion_only_and_empty_extensions(self):
        self.check('a' * 500, 'b' * 500, 1000)
        self.check('a' * 500, 'a' * 500, 0)
        self.check('a' * 500, 'a' * 499, 1)
        self.check('ab' * 250, 'ba' * 250, 2)
        self.check('sea', 'eat', 2)
        self.check('', 'abc', 3)


if __name__ == '__main__':
    unittest.main()
