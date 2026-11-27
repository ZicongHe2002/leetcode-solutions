class Solution:
    def minKBitFlips(self, nums, k):
        ending = [0] * (len(nums) + 1)
        parity = flips = 0
        for index,value in enumerate(nums):
            parity ^= ending[index]
            if value ^ parity == 0:
                if index + k > len(nums):
                    return -1
                flips += 1
                parity ^= 1
                ending[index + k] ^= 1
        return flips
