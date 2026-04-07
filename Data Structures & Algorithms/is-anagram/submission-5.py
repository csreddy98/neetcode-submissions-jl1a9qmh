class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(s.split().sort(), t.split())
        return s.split().sort() == t.split().sort()