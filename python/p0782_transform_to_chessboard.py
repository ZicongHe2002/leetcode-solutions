class Solution:
    def movesToChessboard(self, board):
        size = len(board)
        if any(board[0][0] ^ board[row][0] ^ board[0][column] ^ board[row][column]
               for row in range(size) for column in range(size)):
            return -1
        row_ones = sum(board[row][0] for row in range(size))
        column_ones = sum(board[0])
        if not (size // 2 <= row_ones <= (size + 1) // 2
                and size // 2 <= column_ones <= (size + 1) // 2):
            return -1
        row_mismatch = sum(board[row][0] != row % 2 for row in range(size))
        column_mismatch = sum(board[0][column] != column % 2 for column in range(size))
        if size % 2:
            if row_mismatch % 2:
                row_mismatch = size - row_mismatch
            if column_mismatch % 2:
                column_mismatch = size - column_mismatch
        else:
            row_mismatch = min(row_mismatch, size - row_mismatch)
            column_mismatch = min(column_mismatch, size - column_mismatch)
        return (row_mismatch + column_mismatch) // 2
