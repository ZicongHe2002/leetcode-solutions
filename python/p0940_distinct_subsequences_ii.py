class Solution:
    def distinctSubseqII(self, s):
        modulus = 10**9 + 7
        total = 1
        previous = {}
        for char in s:
            following = (2 * total - previous.get(char,0)) % modulus
            previous[char] = total
            total = following
        return (total - 1) % modulus
