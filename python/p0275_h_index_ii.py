class Solution:
    def hIndex(self, citations):
        size = len(citations)
        left, right = 0, size
        while left < right:
            middle = (left + right) // 2
            if citations[middle] >= size - middle:
                right = middle
            else:
                left = middle + 1
        return size - left
