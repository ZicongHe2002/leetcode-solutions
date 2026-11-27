class Solution:
    def minDeletionSize(self, strs):
        ordered = [False] * (len(strs) - 1)
        deleted = 0
        for column in range(len(strs[0])):
            if any(not ordered[row] and strs[row][column] > strs[row + 1][column]
                   for row in range(len(strs) - 1)):
                deleted += 1
                continue
            for row in range(len(strs) - 1):
                if strs[row][column] < strs[row + 1][column]:
                    ordered[row] = True
        return deleted
