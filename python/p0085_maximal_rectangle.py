class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * (len(matrix[0]) + 1)
        best = 0
        for row in matrix:
            for column, value in enumerate(row):
                heights[column] = heights[column] + 1 if value == '1' else 0
            pending = []
            for right, current in enumerate(heights):
                while pending and heights[pending[-1]] > current:
                    height = heights[pending.pop()]
                    left = pending[-1] if pending else -1
                    best = max(best, height * (right - left - 1))
                pending.append(right)
        return best
