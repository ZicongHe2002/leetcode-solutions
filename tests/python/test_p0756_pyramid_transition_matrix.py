import unittest
from itertools import product

from python.p0756_pyramid_transition_matrix import Solution


TRIPLES = [''.join(chars) for chars in product('AB', repeat=3)]
BIT = {triple: 1 << index for index, triple in enumerate(TRIPLES)}


def complete_assignments_required_masks(bottom):
    lengths = list(range(len(bottom) - 1, 0, -1))
    required = set()
    for flat in product('AB', repeat=sum(lengths)):
        offset, lower, mask = 0, bottom, 0
        for length in lengths:
            upper = ''.join(flat[offset:offset + length])
            offset += length
            for index, value in enumerate(upper):
                mask |= BIT[lower[index:index + 2] + value]
            lower = upper
        required.add(mask)
    return required


class PyramidTransitionTests(unittest.TestCase):
    def test_all_binary_rule_sets_against_complete_pyramid_cell_assignments(self):
        checked = 0
        for size in range(2, 5):
            for chars in product('AB', repeat=size):
                bottom = ''.join(chars)
                required = complete_assignments_required_masks(bottom)
                for mask in range(256):
                    allowed = [triple for index, triple in enumerate(TRIPLES) if mask >> index & 1]
                    before = allowed[:]
                    result = Solution().pyramidTransition(bottom, allowed)
                    self.assertIs(type(result), bool)
                    self.assertEqual(result, any(need & mask == need for need in required), (bottom, allowed))
                    self.assertEqual(allowed, before)
                    checked += 1
        self.assertEqual(checked, 7168)

    def test_official_examples_maximum_bottom_and_full_six_character_rules(self):
        self.assertTrue(Solution().pyramidTransition('BCD', ['BCC','CDE','CEA','FFF']))
        self.assertFalse(Solution().pyramidTransition('AAAA', ['AAB','AAC','BCD','BBE','DEF']))
        self.assertFalse(Solution().pyramidTransition('ABCDEF', []))
        self.assertTrue(Solution().pyramidTransition('FFFFFF', ['FFF']))
        full = [''.join(chars) for chars in product('ABCDEF', repeat=3)]
        self.assertEqual(len(full), 216)
        self.assertTrue(Solution().pyramidTransition('ABCDEF', full))
        self.assertFalse(Solution().pyramidTransition('BA', ['ABC']))
        self.assertTrue(Solution().pyramidTransition('AB', ['ABC']))


if __name__ == '__main__':
    unittest.main()
