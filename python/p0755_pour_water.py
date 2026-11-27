class Solution:
    def pourWater(self, heights, volume, k):
        levels = heights[:]
        for _ in range(volume):
            best, index = k, k - 1
            while index >= 0 and levels[index] <= levels[index + 1]:
                if levels[index] < levels[best]:
                    best = index
                index -= 1
            if best == k:
                index = k + 1
                while index < len(levels) and levels[index] <= levels[index - 1]:
                    if levels[index] < levels[best]:
                        best = index
                    index += 1
            levels[best] += 1
        return levels
