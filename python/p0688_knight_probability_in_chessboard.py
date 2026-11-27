class Solution:
    def knightProbability(self, n, k, row, column):
        moves = ((1, 2), (1, -2), (-1, 2), (-1, -2),
                 (2, 1), (2, -1), (-2, 1), (-2, -1))
        ways = [[1] * n for _ in range(n)]
        for _ in range(k):
            following = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    following[r][c] = sum(ways[r + dr][c + dc] for dr, dc in moves
                                          if 0 <= r + dr < n and 0 <= c + dc < n)
            ways = following
        return ways[row][column] / 8**k
