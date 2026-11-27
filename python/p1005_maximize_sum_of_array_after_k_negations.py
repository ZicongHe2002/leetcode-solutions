class Solution:
    def largestSumAfterKNegations(self, nums, k):
        values = sorted(nums)
        for index in range(len(values)):
            if values[index] < 0 and k:
                values[index] = -values[index]
                k -= 1
        answer = sum(values)
        if k % 2:
            answer -= 2 * min(values)
        return answer
