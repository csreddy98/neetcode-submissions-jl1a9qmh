class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1p, s2p = 0, 0
        sorteds1 = sorted(s1)
        while s2p < len(s2):
            if s2[s2p] not in s1:
                s2p += 1
                continue
            subStr = s2[s2p:s2p+len(s1)]
            print(subStr)
            if sorted(subStr) == sorteds1:
                return True
            else:
                s2p += 1
        return False
