class Solution:
    def lenLongestFibSubseq(self, arr):
        position = {value:index for index,value in enumerate(arr)}
        lengths = {}
        best = 0
        for last in range(len(arr)):
            for middle in range(last):
                needed = arr[last] - arr[middle]
                first = position.get(needed,-1)
                if 0 <= first < middle:
                    length = lengths.get((first,middle),2) + 1
                    lengths[middle,last] = length
                    best = max(best,length)
        return best
