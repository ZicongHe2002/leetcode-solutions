class Solution:
    def countBattleships(self, board):
        count = 0
        for row in range(len(board)):
            for column in range(len(board[0])):
                if (board[row][column] == 'X'
                        and (row == 0 or board[row - 1][column] != 'X')
                        and (column == 0 or board[row][column - 1] != 'X')):
                    count += 1
        return count
