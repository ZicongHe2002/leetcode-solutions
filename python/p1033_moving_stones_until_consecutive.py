class Solution:
    def numMovesStones(self, a, b, c):
        left,middle,right = sorted((a,b,c))
        if right - left == 2:
            minimum = 0
        elif min(middle - left,right - middle) <= 2:
            minimum = 1
        else:
            minimum = 2
        return [minimum,right - left - 2]
