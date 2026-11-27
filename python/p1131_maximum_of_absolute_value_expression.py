class Solution:
    def maxAbsValExpr(self, arr1, arr2):
        answer = 0
        for first_sign in (-1, 1):
            for second_sign in (-1, 1):
                low, high = float('inf'), float('-inf')
                for index, (first, second) in enumerate(zip(arr1, arr2)):
                    value = first_sign * first + second_sign * second + index
                    low = min(low, value)
                    high = max(high, value)
                answer = max(answer, high - low)
        return answer
