class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        x, y = 0, 0

        for n in nums:
            tmp = max(y, n + x)
            x = y
            y = tmp
        
        return y