class Solution:
    def anagramMappings(self, nums1, nums2):
        positions = {}
        for index, value in enumerate(nums2):
            positions.setdefault(value, []).append(index)
        return [positions[value].pop() for value in nums1]
