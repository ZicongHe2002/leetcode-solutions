from itertools import permutations
import unittest

from python.p0599_minimum_index_sum_of_two_lists import Solution


def all_matching_pairs(first, second):
    matches = [(i + j, name) for i, name in enumerate(first) for j, other in enumerate(second) if name == other]
    minimum = min(total for total, _ in matches)
    return {name for total, name in matches if total == minimum}


def label(index):
    return ''.join(chr(65 + digit) for digit in (index // 676, index // 26 % 26, index % 26))


class MinimumIndexTests(unittest.TestCase):
    def check(self, first, second, expected):
        before = (first[:], second[:])
        result = Solution().findRestaurant(first, second)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(name) is str for name in result))
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(set(result), expected)
        self.assertEqual((first, second), before)

    def test_all_small_unique_lists_with_common_items_against_all_pairs(self):
        pool = ('A', 'a', 'New York', 'two words')
        lists = [list(values) for size in range(1, 5) for values in permutations(pool, size)]
        self.assertEqual(len(lists), 64)
        cases = 0
        for first in lists:
            for second in lists:
                if set(first).intersection(second):
                    self.check(first, second, all_matching_pairs(first, second))
                    cases += 1
        self.assertEqual(cases, 3964)

    def test_thousand_items_all_ties_late_match_and_exact_name_semantics(self):
        names = [label(index) for index in range(1000)]
        self.check(names, names[::-1], set(names))
        self.check(names, names[500:] + names[:500], {names[0], names[500]})
        self.check(names, ['other' + label(index) for index in range(999)] + [names[-1]], {names[-1]})
        self.check(['Same', 'same', 'two words'], ['same', 'Same', 'two words'], {'Same', 'same'})
        self.check(['a b', 'ab'], ['ab', 'a b'], {'a b', 'ab'})
        self.check(['zero', 'other'], ['zero'], {'zero'})


if __name__ == '__main__':
    unittest.main()
