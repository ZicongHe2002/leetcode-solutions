import string
import unittest
from itertools import permutations, product

from python.p0791_custom_sort_string import Solution


class CustomSortStringTests(unittest.TestCase):
    def check(self, order, text):
        result = Solution().customSortString(order,text)
        self.assertIs(type(result),str)
        self.assertEqual(sorted(result),sorted(text))
        positions = {}
        for index,char in enumerate(result):
            positions.setdefault(char,[]).append(index)
        for index,first in enumerate(order):
            for second in order[index + 1:]:
                if first in positions and second in positions:
                    self.assertLess(max(positions[first]),min(positions[second]),(order,text,result))

    def test_every_small_unique_order_and_text_against_full_permutation_and_pairwise_precedence_contract(self):
        orders = [''.join(chars) for size in range(1,4) for chars in permutations('abc',size)]
        checked = 0
        for order in orders:
            for size in range(1,6):
                for chars in product('abcd',repeat=size):
                    self.check(order,''.join(chars))
                    checked += 1
        self.assertEqual(checked,20460)

    def test_official_examples_maximum_order_and_text_and_absent_priority_characters(self):
        self.check('cba','abcd')
        self.check('bcafg','abcd')
        self.check(string.ascii_lowercase[::-1],''.join(chr(97 + index % 26) for index in range(200)))
        self.check('z','a' * 200)
        self.check('za','a' * 200)
        self.check('a','z' * 199 + 'a')
        self.check('cba','a' * 67 + 'b' * 66 + 'c' * 67)


if __name__ == '__main__':
    unittest.main()
