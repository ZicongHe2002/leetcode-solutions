class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        best = [0] * (len(arr) + 1)
        for end in range(1,len(arr) + 1):
            maximum = 0
            for length in range(1,min(k,end) + 1):
                maximum = max(maximum,arr[end - length])
                best[end] = max(best[end],best[end - length] + length * maximum)
        return best[-1]
