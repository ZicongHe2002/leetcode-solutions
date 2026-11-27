class Solution:
    def longestMountain(self, arr):
        up = down = best = 0
        for index in range(1,len(arr)):
            if (down and arr[index] > arr[index - 1]) or arr[index] == arr[index - 1]:
                up = down = 0
            if arr[index] > arr[index - 1]:
                up += 1
            elif arr[index] < arr[index - 1]:
                down += 1
            if up and down:
                best = max(best,up + down + 1)
        return best
