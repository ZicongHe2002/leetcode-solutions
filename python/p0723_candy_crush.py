class Solution:
    def candyCrush(self, board):
        rows, columns = len(board), len(board[0])
        while True:
            crushed = False
            for row in range(rows):
                for column in range(columns - 2):
                    value = abs(board[row][column])
                    if value and value == abs(board[row][column + 1]) == abs(board[row][column + 2]):
                        for offset in range(3):
                            board[row][column + offset] = -value
                        crushed = True
            for column in range(columns):
                for row in range(rows - 2):
                    value = abs(board[row][column])
                    if value and value == abs(board[row + 1][column]) == abs(board[row + 2][column]):
                        for offset in range(3):
                            board[row + offset][column] = -value
                        crushed = True
            if not crushed:
                return board
            for column in range(columns):
                write = rows - 1
                for row in range(rows - 1, -1, -1):
                    if board[row][column] > 0:
                        board[write][column] = board[row][column]
                        write -= 1
                while write >= 0:
                    board[write][column] = 0
                    write -= 1
