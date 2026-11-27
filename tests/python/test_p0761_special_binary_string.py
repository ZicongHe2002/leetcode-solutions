import unittest
from itertools import product

from python.p0761_special_binary_string import Solution


def is_special(text):
    balance = 0
    for char in text:
        balance += 1 if char == '1' else -1
        if balance < 0:
            return False
    return balance == 0


def all_real_swap_states(text):
    seen, frontier = {text}, [text]
    for state in frontier:
        size = len(state)
        for middle in range(1, size):
            lefts = [left for left in range(middle) if is_special(state[left:middle])]
            rights = [right for right in range(middle + 1, size + 1) if is_special(state[middle:right])]
            for left in lefts:
                for right in rights:
                    moved = state[:left] + state[middle:right] + state[left:middle] + state[right:]
                    if moved not in seen:
                        seen.add(moved)
                        frontier.append(moved)
    return seen


class SpecialBinaryTests(unittest.TestCase):
    def check(self, text, expected):
        result = Solution().makeLargestSpecial(text)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected, text)
        self.assertEqual(len(result), len(text))
        self.assertTrue(is_special(result))
        self.assertEqual(result.count('1'), text.count('1'))

    def test_every_small_special_string_against_reachable_actual_adjacent_swaps(self):
        checked = 0
        for pairs in range(1, 7):
            for bits in product('10', repeat=2 * pairs):
                text = ''.join(bits)
                if is_special(text):
                    self.check(text, max(all_real_swap_states(text)))
                    checked += 1
        self.assertEqual(checked, 196)

    def test_official_example_maximum_nested_depth_and_maximum_flat_blocks(self):
        self.check('11011000', '11100100')
        self.check('10', '10')
        self.check('1' * 25 + '0' * 25, '1' * 25 + '0' * 25)
        self.check('10' * 25, '10' * 25)
        self.check('101100', '110010')


if __name__ == '__main__':
    unittest.main()
