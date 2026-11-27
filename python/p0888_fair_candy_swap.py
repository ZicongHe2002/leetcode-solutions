class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        difference = (sum(aliceSizes) - sum(bobSizes)) // 2
        available = set(bobSizes)
        for alice in aliceSizes:
            bob = alice - difference
            if bob in available:
                return [alice,bob]
        return []
