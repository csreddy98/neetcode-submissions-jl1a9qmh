class Solution:
    def rob(self, nums: List[int]) -> int:
        x, y = 0, 0

        for n in nums:
            tmp = max(n + x, y)
            x = y
            y = tmp
        return y