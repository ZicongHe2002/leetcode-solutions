class Solution:
    def maxChunksToSorted(self, arr):
        largest = -1
        chunks = 0
        for index, value in enumerate(arr):
            largest = max(largest, value)
            if largest == index:
                chunks += 1
        return chunks
