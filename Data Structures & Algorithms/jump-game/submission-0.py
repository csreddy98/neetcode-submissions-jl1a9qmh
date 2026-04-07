class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0

        while pos < len(nums) - 1:
            if nums[pos] == 0:
                return False
            pos += nums[pos]
        print(pos)
        return True if pos == len(nums) - 1 else False