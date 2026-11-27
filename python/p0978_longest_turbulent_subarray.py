class Solution:
    def maxTurbulenceSize(self, arr):
        up = down = best = 1
        for index in range(1,len(arr)):
            if arr[index] > arr[index - 1]:
                up,down = down + 1,1
            elif arr[index] < arr[index - 1]:
                up,down = 1,up + 1
            else:
                up = down = 1
            best = max(best,up,down)
        return best
