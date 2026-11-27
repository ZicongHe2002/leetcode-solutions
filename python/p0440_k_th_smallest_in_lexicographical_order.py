class Solution:
    def findKthNumber(self, n, k):
        prefix = 1
        remaining = k - 1
        while remaining:
            first, following = prefix, prefix + 1
            count = 0
            while first <= n:
                count += min(n + 1, following) - first
                first *= 10
                following *= 10
            if count <= remaining:
                prefix += 1
                remaining -= count
            else:
                prefix *= 10
                remaining -= 1
        return prefix
