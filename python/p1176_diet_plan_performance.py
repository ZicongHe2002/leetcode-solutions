class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        total = 0
        answer = 0
        for index, value in enumerate(calories):
            total += value
            if index >= k:
                total -= calories[index - k]
            if index >= k - 1:
                if total < lower:
                    answer -= 1
                elif total > upper:
                    answer += 1
        return answer
