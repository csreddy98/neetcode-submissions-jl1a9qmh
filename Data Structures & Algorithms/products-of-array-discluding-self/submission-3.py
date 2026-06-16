class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]
        def multiply(arr):
            value = 1
            for a in arr:
                value *= a
            return value
        res[0], res[-1] = 1, 1
        # forward
        for i in range(len(nums) - 1, 0, -1):
            res[i] = multiply(nums[:i])
        # backward
        for i in range(len(nums)-1, 0, -1):
            res[i - 1] *= multiply(nums[i:])
        return res
