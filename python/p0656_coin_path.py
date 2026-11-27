class Solution:
    def cheapestJump(self, coins, maxJump):
        size = len(coins)
        if coins[-1] == -1:
            return []
        best = [float('inf')] * size
        following = [-1] * size
        best[-1] = coins[-1]
        for index in range(size - 2, -1, -1):
            if coins[index] == -1:
                continue
            for target in range(index + 1, min(size, index + maxJump + 1)):
                candidate = coins[index] + best[target]
                if candidate < best[index]:
                    best[index] = candidate
                    following[index] = target
        if best[0] == float('inf'):
            return []
        path, index = [], 0
        while index != -1:
            path.append(index + 1)
            index = following[index]
        return path
