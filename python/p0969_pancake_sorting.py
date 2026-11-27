class Solution:
    def pancakeSort(self, arr):
        values = arr[:]
        flips = []
        for length in range(len(values),1,-1):
            position = values.index(length)
            if position == length - 1:
                continue
            if position:
                values[:position + 1] = values[:position + 1][::-1]
                flips.append(position + 1)
            values[:length] = values[:length][::-1]
            flips.append(length)
        return flips
