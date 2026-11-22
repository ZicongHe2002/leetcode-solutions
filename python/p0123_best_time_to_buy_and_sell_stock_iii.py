class Solution:
    def maxProfit(self, prices):
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        for price in prices:
            buy1, sell1, buy2, sell2 = (
                max(buy1, -price),
                max(sell1, buy1 + price),
                max(buy2, sell1 - price),
                max(sell2, buy2 + price),
            )
        return sell2
