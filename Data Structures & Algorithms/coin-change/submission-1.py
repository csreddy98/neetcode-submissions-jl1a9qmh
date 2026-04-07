class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        coins.sort()
        for i in range(len(coins) - 1, -1, -1):
            while amount - coins[i] >= 0:
                amount -= coins[i]
                res += 1
        

        return res if amount == 0 else -1
