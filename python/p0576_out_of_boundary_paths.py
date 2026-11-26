class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        modulus = 10**9 + 7
        current = [[0] * n for _ in range(m)]
        current[startRow][startColumn] = 1
        escaped = 0
        for _ in range(maxMove):
            following = [[0] * n for _ in range(m)]
            for row in range(m):
                for column in range(n):
                    ways = current[row][column]
                    if ways == 0:
                        continue
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        r, c = row + dr, column + dc
                        if 0 <= r < m and 0 <= c < n:
                            following[r][c] = (following[r][c] + ways) % modulus
                        else:
                            escaped = (escaped + ways) % modulus
            current = following
        return escaped
