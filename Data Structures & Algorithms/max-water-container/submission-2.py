class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        findArea = lambda l, r: min(heights[l], heights[r]) * (r - l)
        l, r = 0, len(heights) - 1
        while l < r:
            area = findArea(l, r)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            result = max(result, area)
        return result