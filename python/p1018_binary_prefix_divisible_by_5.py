class Solution:
    def prefixesDivBy5(self, nums):
        remainder = 0
        answer = []
        for bit in nums:
            remainder = (2 * remainder + bit) % 5
            answer.append(remainder == 0)
        return answer
