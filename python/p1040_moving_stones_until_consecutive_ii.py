class Solution:
    def numMovesStonesII(self, stones):
        values = sorted(stones)
        size = len(values)
        maximum = max(values[-1] - values[1] - size + 2,values[-2] - values[0] - size + 2)
        minimum = size
        left = 0
        for right in range(size):
            while values[right] - values[left] + 1 > size:
                left += 1
            present = right - left + 1
            if present == size - 1 and values[right] - values[left] == size - 2:
                minimum = min(minimum,2)
            else:
                minimum = min(minimum,size - present)
        return [minimum,maximum]
