class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        area = lambda x, y: min(heights[x], heights[y]) * (y - x)
        while l < r:
            res = max(res, area(l, r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res