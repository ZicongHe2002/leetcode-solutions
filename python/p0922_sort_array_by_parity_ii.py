class Solution:
    def sortArrayByParityII(self, nums):
        result = nums[:]
        odd = 1
        for even in range(0,len(result),2):
            if result[even] % 2:
                while result[odd] % 2:
                    odd += 2
                result[even],result[odd] = result[odd],result[even]
                odd += 2
        return result
