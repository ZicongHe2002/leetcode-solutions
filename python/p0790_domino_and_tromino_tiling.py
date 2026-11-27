class Solution:
    def numTilings(self, n):
        if n == 1:
            return 1
        modulus = 10**9 + 7
        before_three, before_two, before_one = 1, 1, 2
        for width in range(3,n + 1):
            before_three, before_two, before_one = before_two, before_one, (2 * before_one + before_three) % modulus
        return before_one
