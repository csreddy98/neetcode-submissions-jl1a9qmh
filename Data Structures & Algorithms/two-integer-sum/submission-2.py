class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in sums:
                return [sums[res], i]
            sums[nums[i]] = i