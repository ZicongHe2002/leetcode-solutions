class Solution:
    def maximumSum(self, arr):
        keep = answer = arr[0]
        deleted = float('-inf')
        for index in range(1, len(arr)):
            value = arr[index]
            deleted = max(deleted + value, keep)
            keep = max(value, keep + value)
            answer = max(answer, keep, deleted)
        return answer
