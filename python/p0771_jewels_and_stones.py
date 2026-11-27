class Solution:
    def numJewelsInStones(self, jewels, stones):
        types = set(jewels)
        return sum(stone in types for stone in stones)
