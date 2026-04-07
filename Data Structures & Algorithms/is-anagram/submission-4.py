class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(s.split().sort(), t.split().sort())
        return s.split().sort() == t.split().sort()