class Solution:
    def gameOfLife(self, board):
        rows, columns = len(board), len(board[0])
        for row in range(rows):
            for column in range(columns):
                neighbors = 0
                for nearby_row in range(max(0, row - 1), min(rows, row + 2)):
                    for nearby_column in range(max(0, column - 1), min(columns, column + 2)):
                        if nearby_row != row or nearby_column != column:
                            neighbors += board[nearby_row][nearby_column] & 1
                alive = board[row][column] & 1
                if neighbors == 3 or (alive and neighbors == 2):
                    board[row][column] |= 2
        for row in range(rows):
            for column in range(columns):
                board[row][column] >>= 1
