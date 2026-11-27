class Solution:
    def mergeStones(self, stones, k):
        size = len(stones)
        if (size - 1) % (k - 1):
            return -1
        prefix = [0]
        for value in stones:
            prefix.append(prefix[-1] + value)
        best = [[0] * size for _ in range(size)]
        for length in range(2,size + 1):
            for left in range(size - length + 1):
                right = left + length - 1
                best[left][right] = min(best[left][middle] + best[middle + 1][right]
                                        for middle in range(left,right,k - 1))
                if (length - 1) % (k - 1) == 0:
                    best[left][right] += prefix[right + 1] - prefix[left]
        return best[0][-1]
