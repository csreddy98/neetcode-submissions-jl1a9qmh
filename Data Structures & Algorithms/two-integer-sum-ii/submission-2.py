class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(numbers)):
            if target - numbers[i] in res:
                return [res[i]+1, i+1]
            res[numbers[i]] = i
        return []
            