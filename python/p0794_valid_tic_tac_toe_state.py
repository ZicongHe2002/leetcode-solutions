class Solution:
    def validTicTacToe(self, board):
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)
        if x_count not in (o_count,o_count + 1):
            return False

        def wins(mark):
            return (any(row == mark * 3 for row in board)
                    or any(all(board[row][column] == mark for row in range(3)) for column in range(3))
                    or all(board[index][index] == mark for index in range(3))
                    or all(board[index][2 - index] == mark for index in range(3)))

        x_wins, o_wins = wins('X'), wins('O')
        if x_wins and o_wins:
            return False
        if x_wins and x_count != o_count + 1:
            return False
        if o_wins and x_count != o_count:
            return False
        return True
