class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = 0
        n = len(nums)
        l, r = 0, n - 1
        while l < n:
            res = math.prod(nums[l:r+1])
            maxProduct = max(res, maxProduct)
            if res > maxProduct:
                maxProduct = res
            r -= 1
            if r < l:
                r = n - 1
                l += 1
        return maxProduct