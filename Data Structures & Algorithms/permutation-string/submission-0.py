class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for r in range(len(s2)-1):
            while s2[r] not in s1:
                r += 1
            if s2[l:r] == s1:
                return True
        return False 