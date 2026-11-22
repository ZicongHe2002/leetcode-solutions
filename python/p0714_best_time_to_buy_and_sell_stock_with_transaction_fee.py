class Solution:
    def maxProfit(self, prices, fee):
        cash = 0
        holding = float('-inf')
        for price in prices:
            cash, holding = max(cash, holding + price - fee), max(holding, cash - price)
        return cash
