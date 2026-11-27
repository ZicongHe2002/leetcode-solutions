class Solution:
    def twoSumLessThanK(self, nums, k):
        ordered = sorted(nums)
        left, right = 0, len(ordered) - 1
        answer = -1
        while left < right:
            total = ordered[left] + ordered[right]
            if total < k:
                answer = max(answer, total)
                left += 1
            else:
                right -= 1
        return answer
