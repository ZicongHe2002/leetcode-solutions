class Solution:
    def largestRectangleArea(self, heights):
        pending = []
        best = 0
        for right in range(len(heights) + 1):
            current = heights[right] if right < len(heights) else 0
            start = right
            while pending and pending[-1][1] > current:
                left, height = pending.pop()
                best = max(best, height * (right - left))
                start = left
            if current and (not pending or pending[-1][1] < current):
                pending.append((start, current))
        return best
