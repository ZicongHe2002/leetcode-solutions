class Solution:
    def checkSubarraySum(self, nums, k):
        earliest = {0: -1}
        remainder = 0
        for index, value in enumerate(nums):
            remainder = (remainder + value) % k
            if remainder in earliest:
                if index - earliest[remainder] >= 2:
                    return True
            else:
                earliest[remainder] = index
        return False
