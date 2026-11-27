from random import randrange


class Solution:
    def wiggleSort(self, nums):
        size = len(nums)
        target = size // 2
        left, right = 0, size - 1
        while left <= right:
            pivot = nums[randrange(left, right + 1)]
            lower = current = left
            upper = right
            while current <= upper:
                if nums[current] < pivot:
                    nums[lower], nums[current] = nums[current], nums[lower]
                    lower += 1
                    current += 1
                elif nums[current] > pivot:
                    nums[current], nums[upper] = nums[upper], nums[current]
                    upper -= 1
                else:
                    current += 1
            if target < lower:
                right = lower - 1
            elif target > upper:
                left = upper + 1
            else:
                median = pivot
                break

        def virtual(index):
            return (1 + 2 * index) % (size | 1)

        first = current = 0
        last = size - 1
        while current <= last:
            index = virtual(current)
            if nums[index] > median:
                destination = virtual(first)
                nums[destination], nums[index] = nums[index], nums[destination]
                first += 1
                current += 1
            elif nums[index] < median:
                destination = virtual(last)
                nums[index], nums[destination] = nums[destination], nums[index]
                last -= 1
            else:
                current += 1
