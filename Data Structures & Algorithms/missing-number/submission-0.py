class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        total = sum(range(smallest, largest + 1))
        diff = abs(total - sum(nums))
        return 0 if diff == 0 else diff