class Solution:
    def rotate(self, nums, k):
        if not nums:
            return
        steps = k % len(nums)
        if steps == 0:
            return

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, steps - 1)
        reverse(steps, len(nums) - 1)
