class Solution:
    def alphabetBoardPath(self, target):
        row = column = 0
        moves = []
        for letter in target:
            nr, nc = divmod(ord(letter) - ord('a'), 5)
            moves.append('U' * max(row - nr, 0))
            moves.append('L' * max(column - nc, 0))
            moves.append('D' * max(nr - row, 0))
            moves.append('R' * max(nc - column, 0))
            moves.append('!')
            row, column = nr, nc
        return ''.join(moves)
