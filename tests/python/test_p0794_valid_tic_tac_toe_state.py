import unittest
from itertools import product

from python.p0794_valid_tic_tac_toe_state import Solution


def actual_legal_game_states():
    lines = (7,56,448,73,146,292,273,84)
    states = set()

    def play(text, x_mask, o_mask, turn):
        if text in states:
            return
        states.add(text)
        if any(mask & line == line for mask in (x_mask,o_mask) for line in lines):
            return
        for index,char in enumerate(text):
            if char == ' ':
                following = text[:index] + turn + text[index + 1:]
                bit = 1 << index
                if turn == 'X':
                    play(following,x_mask | bit,o_mask,'O')
                else:
                    play(following,x_mask,o_mask | bit,'X')

    play(' ' * 9,0,0,'X')
    return states


class ValidTicTacToeTests(unittest.TestCase):
    def check(self, board, expected):
        before = board[:]
        result = Solution().validTicTacToe(board)
        self.assertIs(type(result),bool)
        self.assertEqual(result,expected,board)
        self.assertEqual(board,before)

    def test_all_ternary_boards_against_actual_games_stopping_at_first_win(self):
        reachable = actual_legal_game_states()
        self.assertEqual(len(reachable),5478)
        checked = 0
        for cells in product(' XO',repeat=9):
            text = ''.join(cells)
            self.check([text[:3],text[3:6],text[6:]],text in reachable)
            checked += 1
        self.assertEqual(checked,19683)

    def test_examples_double_winners_post_win_moves_and_intersecting_final_wins(self):
        self.check(['O  ','   ','   '],False)
        self.check(['XOX',' X ','   '],False)
        self.check(['XOX','O O','XOX'],True)
        self.check(['XXX','OOO','   '],False)
        self.check(['XXX','OO ','O  '],False)
        self.check(['XOX','OXO','XOX'],True)
        self.check(['   ','   ','   '],True)


if __name__ == '__main__':
    unittest.main()
