class Solution:
    def partitionDisjoint(self, nums):
        boundary = 0
        left_maximum = prefix_maximum = nums[0]
        for index in range(1,len(nums)):
            prefix_maximum = max(prefix_maximum,nums[index])
            if nums[index] < left_maximum:
                boundary = index
                left_maximum = prefix_maximum
        return boundary + 1
