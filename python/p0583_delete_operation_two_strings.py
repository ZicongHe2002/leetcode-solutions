class Solution:
    def minDistance(self, word1, word2):
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        previous = [0] * (len(word2) + 1)
        for left in word1:
            current = [0] * (len(word2) + 1)
            for column, right in enumerate(word2, 1):
                if left == right:
                    current[column] = previous[column - 1] + 1
                else:
                    current[column] = max(previous[column], current[column - 1])
            previous = current
        return len(word1) + len(word2) - 2 * previous[-1]
