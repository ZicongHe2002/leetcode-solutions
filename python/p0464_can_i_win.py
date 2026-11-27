class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        memo = {}

        def wins(used, remaining):
            if used in memo:
                return memo[used]
            for choice in range(maxChoosableInteger, 0, -1):
                bit = 1 << (choice - 1)
                if used & bit:
                    continue
                if choice >= remaining or not wins(used | bit, remaining - choice):
                    memo[used] = True
                    return True
            memo[used] = False
            return False

        return wins(0, desiredTotal)
