class Solution:
    def arrangeCoins(self, n):
        low, high = 0, n
        while low <= high:
            middle = (low + high) // 2
            required = middle * (middle + 1) // 2
            if required <= n:
                low = middle + 1
            else:
                high = middle - 1
        return high
