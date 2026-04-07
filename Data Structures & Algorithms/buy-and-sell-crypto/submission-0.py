class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x, y = 0, 1
        res = 0
        while y < len(prices):
            if prices[x] < prices[y]:
                profit = prices[y] - prices[x]
                res = max(profit, res)
            else:
                x = y
            y += 1
        return res