class Solution:
    def change(self, amount, coins):
        counts = [0] * (amount + 1)
        counts[0] = 1
        for coin in coins:
            for total in range(coin, amount + 1):
                counts[total] += counts[total - coin]
        return counts[amount]
