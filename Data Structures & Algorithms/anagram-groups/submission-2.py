class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sSorted = ''.join(sorted(s))
            if sSorted not in res:
                res[sSorted] = []
            res[sSorted].append(s)
        return list(res.values())