class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        count = 0
        highest_count = 0
        if len(nums) <= 1:
            return len(nums)
        for i in range(1, len(nums), 1):
            if sorted_nums[i-1] == sorted_nums[i] - 1 or sorted_nums[i-1] == sorted_nums[i]:
                count += 1
                highest_count = count if count > highest_count else highest_count
            else:
                count = 1
        return highest_count
        