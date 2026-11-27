class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        last_too_large = last_in_range = -1
        answer = 0
        for index,value in enumerate(nums):
            if value > right:
                last_too_large = index
            if left <= value <= right:
                last_in_range = index
            answer += max(0,last_in_range - last_too_large)
        return answer
