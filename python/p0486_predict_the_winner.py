class Solution:
    def predictTheWinner(self, nums):
        advantage = nums[:]
        for length in range(2, len(nums) + 1):
            for left in range(len(nums) - length + 1):
                right = left + length - 1
                advantage[left] = max(nums[left] - advantage[left + 1],
                                      nums[right] - advantage[left])
        return advantage[0] >= 0
