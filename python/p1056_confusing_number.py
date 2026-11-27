class Solution:
    def confusingNumber(self, n):
        mapping = {0:0,1:1,6:9,8:8,9:6}
        original = n
        rotated = 0
        while n:
            n,digit = divmod(n,10)
            if digit not in mapping:
                return False
            rotated = 10 * rotated + mapping[digit]
        return rotated != original
