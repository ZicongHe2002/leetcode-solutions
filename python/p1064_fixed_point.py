class Solution:
    def fixedPoint(self, arr):
        left,right = 0,len(arr)
        while left < right:
            middle = (left + right) // 2
            if arr[middle] >= middle:
                right = middle
            else:
                left = middle + 1
        return left if left < len(arr) and arr[left] == left else -1
