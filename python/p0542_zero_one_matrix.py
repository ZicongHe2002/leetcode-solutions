from collections import deque


class Solution:
    def updateMatrix(self, mat):
        if not mat:
            return []
        rows, columns = len(mat), len(mat[0])
        distances = [[-1] * columns for _ in range(rows)]
        pending = deque()
        for row in range(rows):
            for column in range(columns):
                if mat[row][column] == 0:
                    distances[row][column] = 0
                    pending.append((row, column))
        while pending:
            row, column = pending.popleft()
            for nr, nc in ((row - 1, column), (row + 1, column),
                           (row, column - 1), (row, column + 1)):
                if 0 <= nr < rows and 0 <= nc < columns and distances[nr][nc] == -1:
                    distances[nr][nc] = distances[row][column] + 1
                    pending.append((nr, nc))
        return distances
