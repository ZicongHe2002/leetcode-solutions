class Solution:
    def nextGreaterElements(self, nums):
        result = [-1] * len(nums)
        pending = []
        for step in range(2 * len(nums)):
            value = nums[step % len(nums)]
            while pending and nums[pending[-1]] < value:
                result[pending.pop()] = value
            if step < len(nums):
                pending.append(step)
        return result
