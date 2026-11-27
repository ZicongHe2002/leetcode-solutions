import unittest
from itertools import product

from python.p0777_swap_adjacent_in_lr_string import Solution


def all_directed_legal_move_states(start):
    seen, frontier = {start}, [start]
    while frontier:
        state = frontier.pop()
        for index in range(len(state) - 1):
            pair = state[index:index + 2]
            if pair == 'XL':
                moved = state[:index] + 'LX' + state[index + 2:]
            elif pair == 'RX':
                moved = state[:index] + 'XR' + state[index + 2:]
            else:
                continue
            if moved not in seen:
                seen.add(moved)
                frontier.append(moved)
    return seen


class SwapLRTests(unittest.TestCase):
    def check(self, start, end, expected):
        result = Solution().canTransform(start, end)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected, (start[:100], end[:100]))

    def test_every_small_string_pair_against_complete_directed_legal_move_graph(self):
        checked = 0
        for size in range(1, 7):
            texts = [''.join(chars) for chars in product('LRX', repeat=size)]
            for start in texts:
                reachable = all_directed_legal_move_states(start)
                for end in texts:
                    self.check(start, end, end in reachable)
                    checked += 1
        self.assertEqual(checked, 597870)

    def test_official_examples_maximum_length_directions_empty_cells_and_crossing(self):
        self.check('RXXLRXRXL', 'XRLXXRRLX', True)
        self.check('X', 'L', False)
        self.check('R' + 'X' * 9999, 'X' * 9999 + 'R', True)
        self.check('X' * 9999 + 'R', 'R' + 'X' * 9999, False)
        self.check('X' * 9999 + 'L', 'L' + 'X' * 9999, True)
        self.check('L' + 'X' * 9999, 'X' * 9999 + 'L', False)
        self.check('X' * 10000, 'X' * 10000, True)
        self.check('RL' + 'X' * 9998, 'LR' + 'X' * 9998, False)
        self.check('LRXX' * 2500, 'LRXX' * 2500, True)


if __name__ == '__main__':
    unittest.main()
