class Solution:
    def sumSubseqWidths(self, nums):
        values = sorted(nums)
        modulus = 10**9 + 7
        power = 1
        answer = 0
        for index in range(len(values)):
            answer = (answer + (values[index] - values[-1 - index]) * power) % modulus
            power = power * 2 % modulus
        return answer
