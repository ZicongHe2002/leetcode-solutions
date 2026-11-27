class Solution:
    def findInMountainArray(self, target, mountainArr):
        cache = {}

        def read(index):
            if index not in cache:
                cache[index] = mountainArr.get(index)
            return cache[index]

        size = mountainArr.length()
        left, right = 0, size - 1
        while left < right:
            middle = (left + right) // 2
            if read(middle) < read(middle + 1):
                left = middle + 1
            else:
                right = middle
        peak = left

        left, right = 0, peak
        while left <= right:
            middle = (left + right) // 2
            value = read(middle)
            if value == target:
                return middle
            if value < target:
                left = middle + 1
            else:
                right = middle - 1

        left, right = peak + 1, size - 1
        while left <= right:
            middle = (left + right) // 2
            value = read(middle)
            if value == target:
                return middle
            if value > target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
