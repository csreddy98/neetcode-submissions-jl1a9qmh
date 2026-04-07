class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        for arr in triplets:
            res = [max(res[0], arr[0]), max(res[1], arr[1]), max(res[2], arr[2])]
        
        return True if res == target else False