class Solution:
    def jump(self, nums):
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        jumps = layer_end = farthest = 0
        for index in range(len(nums) - 1):
            farthest = max(farthest, index + nums[index])
            if index == layer_end:
                if farthest == layer_end:
                    return -1
                jumps += 1
                layer_end = farthest
                if layer_end >= len(nums) - 1:
                    return jumps
        return -1
