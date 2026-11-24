class Solution:
    def nextGreaterElement(self, nums1, nums2):
        pending, next_value = [], {}
        for value in nums2:
            while pending and pending[-1] < value:
                next_value[pending.pop()] = value
            pending.append(value)
        return [next_value.get(value, -1) for value in nums1]
