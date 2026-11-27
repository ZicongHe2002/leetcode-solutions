class Solution:
    def numEquivDominoPairs(self, dominoes):
        counts = {}
        answer = 0
        for first, second in dominoes:
            key = (min(first, second), max(first, second))
            answer += counts.get(key, 0)
            counts[key] = counts.get(key, 0) + 1
        return answer
