class Solution:
    def uniquePaths(self, m, n):
        columns = min(m, n)
        paths = [1] * columns
        for _ in range(max(m, n) - 1):
            for column in range(1, columns):
                paths[column] += paths[column - 1]
        return paths[-1]
