class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return s.split('').sort() == t.split('').sort()