class Solution:
    def search(self, reader, target):
        low, high = 0, 1
        while reader.get(high) < target:
            low = high + 1
            high *= 2
        while low <= high:
            middle = (low + high) // 2
            value = reader.get(middle)
            if value == target:
                return middle
            if value < target:
                low = middle + 1
            else:
                high = middle - 1
        return -1
