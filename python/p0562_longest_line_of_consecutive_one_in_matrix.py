class Solution:
    def longestLine(self, mat):
        if not mat or not mat[0]:
            return 0
        columns = len(mat[0])
        vertical = [0] * columns
        diagonal = [0] * (columns + 1)
        anti_diagonal = [0] * (columns + 1)
        best = 0
        for row in mat:
            horizontal = 0
            next_diagonal = [0] * (columns + 1)
            next_anti_diagonal = [0] * (columns + 1)
            for column, value in enumerate(row):
                if value == 0:
                    horizontal = vertical[column] = 0
                    continue
                horizontal += 1
                vertical[column] += 1
                next_diagonal[column + 1] = diagonal[column] + 1
                next_anti_diagonal[column] = anti_diagonal[column + 1] + 1
                best = max(best, horizontal, vertical[column],
                           next_diagonal[column + 1], next_anti_diagonal[column])
            diagonal, anti_diagonal = next_diagonal, next_anti_diagonal
        return best
