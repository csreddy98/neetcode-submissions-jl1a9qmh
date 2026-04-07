class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        x, y = 0, 1
        if len(prices) > 1:
            while y < len(prices) - 1:
                if prices[y] > prices[x]:
                    res = max(res, prices[y] - prices[x])
                else:
                    x = y
                y += 1
        return res