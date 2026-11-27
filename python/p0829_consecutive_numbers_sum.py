class Solution:
    def consecutiveNumbersSum(self, n):
        length = 1
        answer = 0
        while length * (length + 1) // 2 <= n:
            remainder = n - length * (length - 1) // 2
            if remainder % length == 0:
                answer += 1
            length += 1
        return answer
