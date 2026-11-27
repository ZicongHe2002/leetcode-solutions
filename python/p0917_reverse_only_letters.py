class Solution:
    def reverseOnlyLetters(self, s):
        result = list(s)
        left,right = 0,len(result) - 1
        while left < right:
            if not result[left].isalpha():
                left += 1
            elif not result[right].isalpha():
                right -= 1
            else:
                result[left],result[right] = result[right],result[left]
                left += 1
                right -= 1
        return ''.join(result)
