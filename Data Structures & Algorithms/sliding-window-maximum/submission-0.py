class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxVals = []
        while l + k <= len(nums):
            window = nums[l:l+k]
            maxVals.append(max(window))
            l += 1
        return maxVals