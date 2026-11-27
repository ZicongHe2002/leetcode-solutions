class Solution:
    def longestWPI(self, hours):
        first = {0: -1}
        score = answer = 0
        for index, duration in enumerate(hours):
            score += 1 if duration > 8 else -1
            if score > 0:
                answer = index + 1
            elif score - 1 in first:
                answer = max(answer, index - first[score - 1])
            first.setdefault(score, index)
        return answer
