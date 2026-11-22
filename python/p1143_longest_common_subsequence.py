class Solution:
    def longestCommonSubsequence(self, text1, text2):
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        lengths = [0] * (len(text2) + 1)
        for left in text1:
            diagonal = 0
            for column, right in enumerate(text2, 1):
                above = lengths[column]
                if left == right:
                    lengths[column] = diagonal + 1
                else:
                    lengths[column] = max(above, lengths[column - 1])
                diagonal = above
        return lengths[-1]
