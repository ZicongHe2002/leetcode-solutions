class Solution:
    def orderlyQueue(self, s, k):
        if k == 1:
            return min(s[index:] + s[:index] for index in range(len(s)))
        return ''.join(sorted(s))
