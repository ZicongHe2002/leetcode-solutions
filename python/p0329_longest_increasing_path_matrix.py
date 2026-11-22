from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix):
        rows, columns = len(matrix), len(matrix[0])
        degree = [[0] * columns for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for column in range(columns):
                degree[row][column] = sum(
                    matrix[nr][nc] > matrix[row][column]
                    for nr, nc in ((row - 1, column), (row + 1, column),
                                   (row, column - 1), (row, column + 1))
                    if 0 <= nr < rows and 0 <= nc < columns)
                if degree[row][column] == 0:
                    queue.append((row, column))
        length = 0
        while queue:
            length += 1
            for _ in range(len(queue)):
                row, column = queue.popleft()
                for nr, nc in ((row - 1, column), (row + 1, column),
                               (row, column - 1), (row, column + 1)):
                    if 0 <= nr < rows and 0 <= nc < columns and matrix[nr][nc] < matrix[row][column]:
                        degree[nr][nc] -= 1
                        if degree[nr][nc] == 0:
                            queue.append((nr, nc))
        return length
