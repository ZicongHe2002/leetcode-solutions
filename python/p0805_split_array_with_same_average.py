class Solution:
    def splitArraySameAverage(self, nums):
        size = len(nums)
        if size == 1:
            return False
        total = sum(nums)
        transformed = [size * value - total for value in nums]
        middle = size // 2

        def subset_sums(values):
            sums = [0]
            for value in values:
                sums += [previous + value for previous in sums]
            return sums

        left = set(subset_sums(transformed[:middle])[1:])
        if 0 in left:
            return True
        right = subset_sums(transformed[middle:])
        for mask,value in enumerate(right[1:],1):
            if value == 0:
                return True
            if mask != len(right) - 1 and -value in left:
                return True
        return False
