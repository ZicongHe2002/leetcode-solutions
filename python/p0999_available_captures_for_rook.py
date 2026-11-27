class Solution:
    def numRookCaptures(self, board):
        row,column = next((row,column) for row in range(8) for column in range(8) if board[row][column] == 'R')
        captures = 0
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = row + dr,column + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'B':
                    break
                if board[nr][nc] == 'p':
                    captures += 1
                    break
                nr += dr
                nc += dc
        return captures
