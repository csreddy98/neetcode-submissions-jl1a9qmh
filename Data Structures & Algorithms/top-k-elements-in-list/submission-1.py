class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        op = defaultdict(int)
        for i in range(len(nums)):
            op[nums[i]] += 1
        
        return op.values
