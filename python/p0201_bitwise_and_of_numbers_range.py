class Solution:
    def rangeBitwiseAnd(self, left, right):
        shifted = 0
        while left != right:
            left >>= 1
            right >>= 1
            shifted += 1
        return left << shifted
