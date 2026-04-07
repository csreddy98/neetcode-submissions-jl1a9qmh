class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = {}
        for x in nums:
            topK[x] = 1 + topK.get(x, 0)
        sortedTopK = dict(sorted(topK.items(), key=lambda item: item[1], reverse=True))
        print(sortedTopK)
        return list(sortedTopK)[:k]
        