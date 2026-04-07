class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numset = set(nums)
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i in numset:
            freq[count[i]].append(i)
        res = []
        while len(res) != k:
            for i in freq.pop():
                res.append(i)
        return res
