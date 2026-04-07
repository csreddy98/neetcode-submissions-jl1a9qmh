class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        Hmap = {}
        for i in range(len(s)):
            Hmap[s[i]] = i
        
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, Hmap[c]) 

            if i == end:
                res.append(size)
                size = 0
        return res