class Solution:
    def advantageCount(self, nums1, nums2):
        opponents = sorted((value,index) for index,value in enumerate(nums2))
        left,right = 0,len(opponents) - 1
        answer = [0] * len(nums1)
        for value in sorted(nums1):
            if value > opponents[left][0]:
                answer[opponents[left][1]] = value
                left += 1
            else:
                answer[opponents[right][1]] = value
                right -= 1
        return answer
