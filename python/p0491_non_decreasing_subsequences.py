class Solution:
    def findSubsequences(self, nums):
        result = []
        path = []

        def search(start):
            if len(path) >= 2:
                result.append(path[:])
            used = set()
            for index in range(start, len(nums)):
                value = nums[index]
                if value in used or (path and value < path[-1]):
                    continue
                used.add(value)
                path.append(value)
                search(index + 1)
                path.pop()

        search(0)
        return result
