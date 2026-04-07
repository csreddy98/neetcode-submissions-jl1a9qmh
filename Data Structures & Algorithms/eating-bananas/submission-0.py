import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best_val = r
        while l <= r:
            mid = (l + r) // 2
            time = self.computeBananas(piles, mid)
            if time <= h:
                best_val = mid
                r = mid - 1
            else:
                l = mid + 1 
        return best_val
    
    def computeBananas(self, piles, x) -> int:
        res = 0
        for i in piles:
            res += math.ceil(i / x)
        return res