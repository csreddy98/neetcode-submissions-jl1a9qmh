class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i, a in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and a == nums[i-1]:
                continue
            while l < r:
                tmp = a + nums[l] + nums[r]
                if tmp == 0:
                    print("Appending")
                    res.append([a, nums[l], nums[r]])
                if tmp > 0:
                    r -= 1
                else:
                    l += 1
        return res