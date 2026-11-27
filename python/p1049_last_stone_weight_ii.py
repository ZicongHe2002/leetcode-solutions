class Solution:
    def lastStoneWeightII(self, stones):
        total = sum(stones)
        half = total // 2
        possible = [False] * (half + 1)
        possible[0] = True
        for weight in stones:
            for subtotal in range(half,weight - 1,-1):
                possible[subtotal] = possible[subtotal] or possible[subtotal - weight]
        for subtotal in range(half,-1,-1):
            if possible[subtotal]:
                return total - 2 * subtotal
