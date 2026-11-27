class Solution:
    def pathSum(self, nums):
        values = {number // 10: number % 10 for number in nums}
        prefixes = {}
        total = 0
        for number in nums:
            key, value = divmod(number, 10)
            depth, position = divmod(key, 10)
            parent = (depth - 1) * 10 + (position + 1) // 2
            prefixes[key] = value + prefixes.get(parent, 0)
            left = (depth + 1) * 10 + 2 * position - 1
            if left not in values and left + 1 not in values:
                total += prefixes[key]
        return total
