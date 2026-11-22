from collections import Counter


class Solution:
    def exist(self, board, word):
        if not word:
            return True
        if not board or not board[0] or len(word) > len(board) * len(board[0]):
            return False
        counts = Counter(letter for row in board for letter in row)
        if Counter(word) - counts:
            return False
        rows, columns = len(board), len(board[0])
        visited = set()

        def visit(row, column, index):
            if board[row][column] != word[index]:
                return False
            if index + 1 == len(word):
                return True
            visited.add((row, column))
            for nr, nc in ((row - 1, column), (row + 1, column),
                           (row, column - 1), (row, column + 1)):
                if (0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in visited
                        and visit(nr, nc, index + 1)):
                    visited.remove((row, column))
                    return True
            visited.remove((row, column))
            return False

        return any(visit(row, column, 0) for row in range(rows) for column in range(columns))
