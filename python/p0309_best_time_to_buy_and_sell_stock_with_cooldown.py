class Solution:
    def maxProfit(self, prices):
        holding = sold = float('-inf')
        resting = 0
        for price in prices:
            holding, sold, resting = (
                max(holding, resting - price),
                holding + price,
                max(resting, sold),
            )
        return max(resting, sold)
