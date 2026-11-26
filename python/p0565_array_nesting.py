class Solution:
    def arrayNesting(self, nums):
        visited = [False] * len(nums)
        best = 0
        for start in range(len(nums)):
            if visited[start]:
                continue
            current, length = start, 0
            while not visited[current]:
                visited[current] = True
                length += 1
                current = nums[current]
            best = max(best, length)
        return best
