from collections import deque


class Solution:
    def updateBoard(self, board, click):
        rows, columns = len(board), len(board[0])
        start = tuple(click)
        if board[start[0]][start[1]] == 'M':
            board[start[0]][start[1]] = 'X'
            return board

        def neighbors(row, column):
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = row + dr, column + dc
                    if (dr or dc) and 0 <= nr < rows and 0 <= nc < columns:
                        yield nr, nc

        queue, seen = deque([start]), {start}
        while queue:
            row, column = queue.popleft()
            mines = sum(board[nr][nc] == 'M' for nr, nc in neighbors(row, column))
            if mines:
                board[row][column] = str(mines)
            else:
                board[row][column] = 'B'
                for cell in neighbors(row, column):
                    if board[cell[0]][cell[1]] == 'E' and cell not in seen:
                        seen.add(cell)
                        queue.append(cell)
        return board
