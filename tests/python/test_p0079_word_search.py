import unittest
from itertools import product

from python.p0079_word_search import Solution


def all_path_words(board, max_length):
    words = set()
    pending = [(r, c, frozenset({(r, c)}), value)
               for r, row in enumerate(board) for c, value in enumerate(row)]
    while pending:
        r, c, used, text = pending.pop()
        words.add(text)
        if len(text) == max_length:
            continue
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (nr, nc) not in used:
                pending.append((nr, nc, used | {(nr, nc)}, text + board[nr][nc]))
    return words


class WordSearchTests(unittest.TestCase):
    def check(self, board, word, expected):
        before, rows = [row[:] for row in board], board[:]
        self.assertIs(Solution().exist(board, word), expected)
        self.assertEqual(board, before)
        for actual, original in zip(board, rows):
            self.assertIs(actual, original)

    def test_all_small_binary_boards_and_words_against_all_paths(self):
        grids = checks = 0
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3)]:
            length = min(5, height * width + 1)
            for values in product('ab', repeat=height * width):
                board = [list(values[r * width:(r + 1) * width]) for r in range(height)]
                words = all_path_words(board, length)
                grids += 1
                for size in range(1, length + 1):
                    for letters in product('ab', repeat=size):
                        word = ''.join(letters)
                        self.check(board, word, word in words)
                        checks += 1
        self.assertEqual((grids, checks), (90, 5212))

    def test_examples_case_bounds_and_empty_extensions(self):
        board = [list('ABCE'), list('SFCS'), list('ADEE')]
        for word, expected in [('ABCCED', True), ('SEE', True), ('ABCB', False)]:
            self.check(board, word, expected)
        self.check([['A'] * 6 for _ in range(6)], 'A' * 15, True)
        self.check([['A'] * 6 for _ in range(6)], 'A' * 14 + 'B', False)
        self.check([list('aaaaaa')], 'aaaaaaa', False)
        self.check([list('aA')], 'aA', True)
        self.check([list('aA')], 'aa', False)
        self.check([], 'A', False)
        self.check([], '', True)


if __name__ == '__main__':
    unittest.main()
