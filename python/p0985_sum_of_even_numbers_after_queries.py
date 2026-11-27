class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        values = nums[:]
        total = sum(value for value in values if value % 2 == 0)
        result = []
        for change,index in queries:
            if values[index] % 2 == 0:
                total -= values[index]
            values[index] += change
            if values[index] % 2 == 0:
                total += values[index]
            result.append(total)
        return result
