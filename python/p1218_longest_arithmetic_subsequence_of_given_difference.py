class Solution:
    def longestSubsequence(self, arr, difference):
        best = {}
        answer = 0
        for value in arr:
            length = best.get(value - difference, 0) + 1
            best[value] = max(best.get(value, 0), length)
            answer = max(answer, best[value])
        return answer
