from itertools import product
import unittest

from python.p0212_word_search_ii import Solution


def single_word_exists(board, word):
    rows, columns = len(board), len(board[0])

    def search(row, column, index, used):
        if board[row][column] != word[index]:
            return False
        if index + 1 == len(word):
            return True
        used = used | {(row, column)}
        return any(search(nr, nc, index + 1, used)
                   for nr, nc in ((row - 1, column), (row + 1, column),
                                  (row, column - 1), (row, column + 1))
                   if 0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in used)

    return any(search(row, column, 0, set()) for row in range(rows) for column in range(columns))


class MultiWordIndependentSearchTests(unittest.TestCase):
    def check(self, board, words, expected=None):
        before = ([row[:] for row in board], words[:])
        if expected is None:
            expected = {word for word in words if single_word_exists(board, word)}
        result = Solution().findWords(board, words)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(word) is str for word in result))
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(set(result), expected)
        self.assertEqual((board, words), before)

    def test_all_small_binary_letter_boards_and_both_dictionary_orders(self):
        words = [''.join(letters) for length in range(1, 7) for letters in product('ab', repeat=length)]
        boards = checks = 0
        for rows, columns in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2)):
            for values in product('ab', repeat=rows * columns):
                board = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                self.check(board, words)
                self.check(board, list(reversed(words)))
                boards += 1
                checks += 2
        self.assertEqual((len(words), boards, checks), (126, 154, 308))

    def test_maximum_board_dictionary_prefixes_and_no_cell_reuse(self):
        words = ['a' * length for length in range(1, 11)]
        for index in range(29990):
            middle = ''.join(chr(97 + (index // 26**place) % 26) for place in range(4))
            words.append('z' + middle + 'b' * 5)
        self.assertEqual((len(words), len(set(words)), max(map(len, words))), (30000, 30000, 10))
        self.check([['a'] * 12 for _ in range(12)], words, {'a' * length for length in range(1, 11)})
        self.check([['a', 'b']], ['a', 'ab', 'aba'], {'a', 'ab'})
        self.check([['a', 'a'], ['a', 'a']], ['aa', 'aaa', 'aaaa'], {'aa', 'aaa', 'aaaa'})
        self.check([['a']], ['b'], set())


if __name__ == '__main__':
    unittest.main()
