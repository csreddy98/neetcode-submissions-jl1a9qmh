class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        repeats = {}
        numsSet = set(nums)
        for i in nums:
            if i not in repeats:
                repeats[i] = 0
            repeats[i] += 1
            if repeats[i] == 2:
                numsSet.remove(i)
        
        return list(numsSet)[0]
