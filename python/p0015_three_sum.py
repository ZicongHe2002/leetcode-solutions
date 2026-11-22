class Solution:
    def threeSum(self, nums):
        ordered = sorted(nums)
        answer = []
        for first in range(len(ordered) - 2):
            if first and ordered[first] == ordered[first - 1]:
                continue
            if ordered[first] > 0:
                break
            left, right = first + 1, len(ordered) - 1
            while left < right:
                total = ordered[first] + ordered[left] + ordered[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    answer.append([ordered[first], ordered[left], ordered[right]])
                    left += 1
                    right -= 1
                    while left < right and ordered[left] == ordered[left - 1]:
                        left += 1
                    while left < right and ordered[right] == ordered[right + 1]:
                        right -= 1
        return answer
