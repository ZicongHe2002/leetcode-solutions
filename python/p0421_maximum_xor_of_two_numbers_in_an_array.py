class Solution:
    def findMaximumXOR(self, nums):
        answer = mask = 0
        for bit in range(30, -1, -1):
            mask |= 1 << bit
            prefixes = {value & mask for value in nums}
            candidate = answer | (1 << bit)
            if any((candidate ^ prefix) in prefixes for prefix in prefixes):
                answer = candidate
        return answer
