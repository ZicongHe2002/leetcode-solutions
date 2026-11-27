class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        windows = [sum(nums[:k])]
        for end in range(k, len(nums)):
            windows.append(windows[-1] + nums[end] - nums[end - k])
        count = len(windows)
        left = [0] * count
        for index in range(1, count):
            left[index] = index if windows[index] > windows[left[index - 1]] else left[index - 1]
        right = [count - 1] * count
        for index in range(count - 2, -1, -1):
            right[index] = index if windows[index] >= windows[right[index + 1]] else right[index + 1]
        best_sum = -1
        answer = None
        for middle in range(k, count - k):
            first, last = left[middle - k], right[middle + k]
            candidate = (first, middle, last)
            total = windows[first] + windows[middle] + windows[last]
            if total > best_sum or total == best_sum and candidate < answer:
                best_sum, answer = total, candidate
        return list(answer)
