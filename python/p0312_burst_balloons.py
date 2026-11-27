class Solution:
    def maxCoins(self, nums):
        values = [1] + nums + [1]
        size = len(values)
        best = [[0] * size for _ in range(size)]
        for width in range(2, size):
            for left in range(size - width):
                right = left + width
                for last in range(left + 1, right):
                    candidate = (best[left][last] + best[last][right]
                                 + values[left] * values[last] * values[right])
                    if candidate > best[left][right]:
                        best[left][right] = candidate
        return best[0][-1]
