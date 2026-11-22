from collections import deque


class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        rows, columns = len(board), len(board[0])
        safe, queue = set(), deque()

        def mark(row, column):
            if board[row][column] == 'O' and (row, column) not in safe:
                safe.add((row, column))
                queue.append((row, column))

        for row in range(rows):
            mark(row, 0)
            mark(row, columns - 1)
        for column in range(columns):
            mark(0, column)
            mark(rows - 1, column)
        while queue:
            row, column = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if 0 <= nr < rows and 0 <= nc < columns:
                    mark(nr, nc)
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == 'O' and (row, column) not in safe:
                    board[row][column] = 'X'
