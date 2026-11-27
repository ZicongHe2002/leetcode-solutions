class Solution:
    def minDeletionSize(self, strs):
        return sum(any(strs[row][column] > strs[row + 1][column] for row in range(len(strs) - 1))
                   for column in range(len(strs[0])))
