class Solution:
    def grayCode(self, n):
        codes = [0]
        for bit in range(n):
            mask = 1 << bit
            for index in range(len(codes) - 1, -1, -1):
                codes.append(codes[index] | mask)
        return codes
