class Solution:
    def findPermutation(self, s):
        result = list(range(1, len(s) + 2))
        start = 0
        while start < len(s):
            if s[start] == 'I':
                start += 1
                continue
            end = start
            while end < len(s) and s[end] == 'D':
                end += 1
            left, right = start, end
            while left < right:
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1
            start = end
        return result
