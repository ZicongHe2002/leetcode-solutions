class Solution:
    def kConcatenationMaxSum(self, arr, k):
        best = ending = 0
        for index in range(len(arr) * min(k, 2)):
            ending = max(0, ending + arr[index % len(arr)])
            best = max(best, ending)
        if k > 2:
            best += max(0, sum(arr)) * (k - 2)
        return best % (10 ** 9 + 7)
