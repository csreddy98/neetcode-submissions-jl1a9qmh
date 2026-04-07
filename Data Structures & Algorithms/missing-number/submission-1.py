class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        total = sum(range(smallest, largest + 1))
        diff = abs(total - sum(nums))
        if diff == 0:
            return 0 if 0 not in nums else largest + 1
        return diff