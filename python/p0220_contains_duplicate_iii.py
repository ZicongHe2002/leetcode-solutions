class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if indexDiff <= 0 or valueDiff < 0:
            return False
        width = valueDiff + 1
        buckets = {}
        for right, value in enumerate(nums):
            bucket = value // width
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and value - buckets[bucket - 1] <= valueDiff:
                return True
            if bucket + 1 in buckets and buckets[bucket + 1] - value <= valueDiff:
                return True
            buckets[bucket] = value
            if right >= indexDiff:
                expired = nums[right - indexDiff] // width
                del buckets[expired]
        return False
