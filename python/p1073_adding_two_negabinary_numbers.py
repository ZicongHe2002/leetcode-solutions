class Solution:
    def addNegabinary(self, arr1, arr2):
        first,second = len(arr1) - 1,len(arr2) - 1
        carry = 0
        result = []
        while first >= 0 or second >= 0 or carry:
            total = carry
            if first >= 0:
                total += arr1[first]
                first -= 1
            if second >= 0:
                total += arr2[second]
                second -= 1
            bit = total & 1
            result.append(bit)
            carry = (total - bit) // -2
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        result.reverse()
        return result
