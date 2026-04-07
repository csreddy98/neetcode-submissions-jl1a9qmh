class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0

        def dfs(amount):
            if amount == 0:
                return 0
            res = float("infinity")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            return res
        
        
        res = dfs(amount)
        return -1 if res == float("infinity") else res
