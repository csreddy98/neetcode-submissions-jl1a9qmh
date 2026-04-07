class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            res = x-y
            if res != 0:
                heapq.heappush(stones, res)
        
        return abs(stones[0]) if len(stones) > 0 else 0