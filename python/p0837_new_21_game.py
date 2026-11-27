class Solution:
    def new21Game(self, n, k, maxPts):
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        if n < k:
            return 0.0
        probability = [0.0] * (n + 1)
        probability[0] = 1.0
        window = 1.0
        answer = 0.0
        for score in range(1,n + 1):
            probability[score] = window / maxPts
            if score < k:
                window += probability[score]
            else:
                answer += probability[score]
            leaving = score - maxPts
            if 0 <= leaving < k:
                window -= probability[leaving]
        return answer
