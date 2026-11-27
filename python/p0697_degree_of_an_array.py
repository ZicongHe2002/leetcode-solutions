class Solution:
    def findShortestSubArray(self, nums):
        stats = {}
        for index, value in enumerate(nums):
            if value not in stats:
                stats[value] = [1, index, index]
            else:
                stats[value][0] += 1
                stats[value][2] = index
        degree = max(record[0] for record in stats.values())
        return min(last - first + 1 for count, first, last in stats.values() if count == degree)
