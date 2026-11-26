class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return False
        window = set()
        for right, value in enumerate(nums):
            if value in window:
                return True
            window.add(value)
            if right >= k:
                window.remove(nums[right - k])
        return False
