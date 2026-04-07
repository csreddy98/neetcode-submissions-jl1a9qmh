class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setx = {}
        for i in range(len(nums)):
            if nums[i] in setx:
                return [setx[nums[i]], i]
            setx[target - nums[i]] = i
