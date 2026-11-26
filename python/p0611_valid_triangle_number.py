class Solution:
    def triangleNumber(self, nums):
        sides = sorted(nums)
        triangles = 0
        for largest in range(2, len(sides)):
            left, right = 0, largest - 1
            while left < right:
                if sides[left] + sides[right] > sides[largest]:
                    triangles += right - left
                    right -= 1
                else:
                    left += 1
        return triangles
