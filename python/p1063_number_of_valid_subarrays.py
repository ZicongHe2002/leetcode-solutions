class Solution:
    def validSubarrays(self, nums):
        starts = []
        answer = 0
        for value in nums:
            while starts and starts[-1] > value:
                starts.pop()
            starts.append(value)
            answer += len(starts)
        return answer
