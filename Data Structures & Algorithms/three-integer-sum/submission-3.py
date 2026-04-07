class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for a, i in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmp = a + nums[l] + nums[r]
                print(a, tmp)
                if tmp == 0:
                    res.append([i, l, r])
                if tmp > 0:
                    r -= 1
                else:
                    l += 1
        return res