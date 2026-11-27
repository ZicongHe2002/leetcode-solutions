class Solution:
    def maxScoreSightseeingPair(self, values):
        left_best = values[0]
        answer = 0
        for right in range(1,len(values)):
            answer = max(answer,left_best + values[right] - right)
            left_best = max(left_best,values[right] + right)
        return answer
