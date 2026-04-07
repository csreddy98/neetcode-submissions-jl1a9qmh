class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        count = 1
        highest_count = 0
        if len(sorted_nums) <= 1:
            return len(sorted_nums)
        for i in range(1, len(sorted_nums), 1):
            if sorted_nums[i-1] == sorted_nums[i] - 1:
                count += 1
                highest_count = max(highest_count, count)
            else:
                count = 1
        return highest_count
        