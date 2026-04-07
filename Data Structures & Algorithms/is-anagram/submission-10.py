class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mapS = {}
        mapT = {}
        
        for i in range(len(s)):
            if s[i] not in mapS:
                mapS[s[i]] = 0
            if t[i] not in mapT:
                mapT[t[i]] = 0
            mapS[s[i]] += 1
            mapT[t[i]] += 1
        return mapS == mapT