class Solution:
    def addToArrayForm(self, num, k):
        result = []
        position = len(num) - 1
        carry = k
        while position >= 0 or carry:
            if position >= 0:
                carry += num[position]
            carry,digit = divmod(carry,10)
            result.append(digit)
            position -= 1
        result.reverse()
        return result
